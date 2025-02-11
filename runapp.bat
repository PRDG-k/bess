@echo off
start cmd /k "uvicorn main:app --host 0.0.0.0 --port 8000 --reload"
timeout /t 3
start cmd /k "streamlit run app.py"
exit
