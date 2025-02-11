from fastapi import FastAPI, WebSocket
import pandas as pd
import numpy as np
import datetime
from predictor import predict_solar, predict_load
from scheduler import optimize_ess
from database import save_to_db, get_latest_data

app = FastAPI()

# 실시간 데이터 업데이트 (WebSocket)
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        now = datetime.datetime.now()
        solar_pred = predict_solar(now)
        load_pred = predict_load(now)
        ess_schedule = optimize_ess(solar_pred, load_pred)
        
        data = {
            "time": now.strftime("%Y-%m-%d %H:%M:%S"),
            "solar_pred": solar_pred,
            "load_pred": load_pred,
            "ess_schedule": ess_schedule
        }
        save_to_db(data)  # DB 저장
        await websocket.send_json(data)

@app.get("/latest")
def get_latest():
    return get_latest_data()
