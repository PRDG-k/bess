import datetime
import numpy as np

def predict_solar():
    """
    전날의 24시간에 대해 태양광 발전량을 예측합니다.
    - 전날 날짜를 기준으로 0시부터 23시까지 각 시간별 예측값을 계산합니다.
    - 발전은 6시부터 18시 사이에 발생하며, 간단한 선형 패턴과 무작위 요인을 적용합니다.
    """
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    predictions = []
    for hour in range(24):
        if 6 <= hour <= 18:
            # 예를 들어, 정오(12시)를 최대 발전량으로 잡고, 양쪽으로 선형 감소
            base = (1 - abs(hour - 12) / 6) * 1000
            # 간단한 랜덤 요인 (0.8 ~ 1.2)
            factor = np.random.uniform(0.8, 1.2)
            pred = base * factor
        else:
            pred = 0
        # 전날의 해당 시간으로 datetime 생성
        dt = datetime.datetime.combine(yesterday, datetime.time(hour, 0))
        predictions.append({
            "time": dt.strftime("%Y-%m-%d %H:%M:%S"),
            "predicted": pred
        })
    return predictions

def actual_solar():
    """
    오늘의 24시간 실제 발전량을 시뮬레이션합니다.
    실제 환경에서는 센서 데이터나 DB의 실제 측정값을 읽어오겠지만,
    여기서는 전형적인 패턴에 약간의 변동을 주어 시뮬레이션합니다.
    """
    today = datetime.date.today()
    actuals = []
    for hour in range(24):
        if 6 <= hour <= 18:
            base = (1 - abs(hour - 12) / 6) * 1000
            # 실제 측정치는 예측보다 약간 다를 수 있으므로 다른 무작위 요인을 적용
            factor = np.random.uniform(0.75, 1.25)
            actual = base * factor
        else:
            actual = 0
        dt = datetime.datetime.combine(today, datetime.time(hour, 0))
        actuals.append({
            "time": dt.strftime("%Y-%m-%d %H:%M:%S"),
            "actual": actual
        })
    return actuals




def predict_load(now=None):
    """ 부하 예측 (간단한 패턴 기반) """
    if now is None:
        now = datetime.datetime.now()
    
    hour = now.hour
    base_load = 500  # 기본 부하
    peak_factor = 1.5 if 18 <= hour <= 22 else 1.0  # 저녁 피크
    return base_load * peak_factor
