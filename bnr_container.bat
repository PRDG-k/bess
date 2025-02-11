@echo off
REM Docker 이미지를 빌드합니다.
docker build --no-cache -t myapp .

REM Docker 컨테이너를 실행합니다. (포트 8000과 8501을 매핑)
docker run -v "%CD%":/app -p 8000:8000 -p 8501:8501 myapp


REM 컨테이너 실행 후 터미널이 바로 닫히지 않도록 대기
pause
