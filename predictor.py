import numpy as np
import datetime

def predict_solar(now=None):
    """ 태양광 발전량 예측 """
    if now is None:
        now = datetime.datetime.now()
    
    hour = now.hour
    weather_factor = np.random.uniform(0.8, 1.2)  # 날씨 영향 (간단한 랜덤 요소)
    
    if 6 <= hour <= 18:
        power = max(0, (1 - abs(hour - 12) / 6) * 1000 * weather_factor)
    else:
        power = 0  # 밤에는 발전량 없음
    return power

def predict_load(now=None):
    """ 부하 예측 (간단한 패턴 기반) """
    if now is None:
        now = datetime.datetime.now()
    
    hour = now.hour
    base_load = 500  # 기본 부하
    peak_factor = 1.5 if 18 <= hour <= 22 else 1.0  # 저녁 피크
    return base_load * peak_factor
