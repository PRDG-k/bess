#!/bin/bash
# run.sh

# FastAPI 서버 실행 (백그라운드 실행)
uvicorn main:app --host 0.0.0.0 --port 8000 --reload &


# Streamlit 애플리케이션 실행 (포그라운드 실행)
# streamlit run app.py
streamlit run app.py --server.runOnSave true
