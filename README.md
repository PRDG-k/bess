# 태양광 발전량 예측 및 BESS 스케줄링 시스템

## 📌 프로젝트 개요
태양광 발전량을 실시간으로 예측하고, 에너지 저장 시스템(BESS, Battery Energy Storage System)의 효율적인 스케줄링을 수행하는 애플리케이션입니다.

## 📊 주요 기능
- **태양광 발전량 예측**: 실시간 기상 데이터를 활용한 발전량 예측
- **BESS 스케줄링**: 예측된 발전량과 부하를 기반으로 충/방전 최적화
- **실시간 비교 분석**: 예측값과 실제값을 실시간으로 비교 및 시각화
- **하이브리드 아키텍처**: 웹 기반 UI와 로컬에서 수행되는 고성능 계산

## 🛠️ 기술 스택
- **프론트엔드**: Streamlit (실시간 데이터 시각화 및 사용자 인터페이스)
- **백엔드**: FastAPI (API 제공 및 WebSocket 기반 실시간 데이터 전송)
- **데이터베이스**: PostgreSQL (정형 데이터 저장), InfluxDB (시계열 데이터 저장)
- **연산 및 최적화**: Python, PuLp

## 📈 시스템 구조
1. **데이터 수집**: 기상청에서 실시간 기상 데이터 수집
2. **데이터 저장**: 발전량 및 기상 데이터를 PostgreSQL 및 InfluxDB에 저장
3. **예측 모델**: 기상 데이터를 활용해 태양광 발전량을 실시간 예측
4. **BESS 스케줄링**: 예측값과 부하를 기반으로 최적 충/방전 일정 수립
5. **시각화 및 분석**: Streamlit을 통한 실시간 데이터 비교 및 시각화

## 📊 예측 모델
- **특징 선택(Feature Selection)**:
    - '지면온도(\u00b0C)', '기온(\u00b0C)', '풍속', '습도(%)', '남북바람성분', '1시간기온', '습도', '풍향', '동서바람성분'
    - 신규 기상 변수만 특징 선택 수행
- **모델 업데이트**: 실시간 데이터 기반 예측 모델 주기적 재학습

## 📦 설치 및 실행 방법
### 사전 요구사항
- Python 3.10 이상
- PostgreSQL 및 InfluxDB 설치

### 설치 과정
```bash
# 저장소 클론
git clone <repository_url>
cd solar-bess-scheduler

# 가상환경 설정
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate

# 필수 패키지 설치
pip install -r requirements.txt

# 데이터베이스 설정 (PostgreSQL, InfluxDB)
python setup_db.py

# 애플리케이션 실행
uvicorn main:app --reload

# Streamlit 대시보드 실행
streamlit run dashboard.py
```

## 📌 사용 예제
1. 실시간 예측값과 실제 발전량 비교
2. 최적화된 BESS 충/방전 일정 확인

## 📊 향후 개선 사항
- 더 정교한 예측 모델 도입 (딥러닝 기반 시계열 분석)
- 다양한 기상 변수 추가
- 사용자 맞춤형 스케줄링 기능 강화

