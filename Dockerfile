# Dockerfile
FROM python:3.10

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements.txt .
COPY config.env .

RUN pip install --upgrade pip && pip install -r requirements.txt && pip list

# 애플리케이션 코드 복사
COPY . .

# run.sh 스크립트 실행 권한 부여
RUN chmod +x run.sh

# uvicorn은 8000번, streamlit은 기본 8501번 포트를 사용하므로 노출
EXPOSE 8000 8501

# 컨테이너 시작 시 run.sh 실행
CMD ["./run.sh"]
