import streamlit as st
import pandas as pd
import asyncio
import websockets
import json

st.title("태양광 예측 및 ESS 최적화 대시보드")

# 웹소켓을 통해 실시간 데이터 수신
async def fetch_data():
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        while True:
            data = await websocket.recv()
            data = json.loads(data)
            return data

# 데이터 업데이트
if st.button("데이터 업데이트"):
    data = asyncio.run(fetch_data())
    st.session_state["latest_data"] = data

# 데이터 시각화
if "latest_data" in st.session_state:
    data = st.session_state["latest_data"]
    df = pd.DataFrame([data])
    st.write(df)
    st.line_chart(df[["solar_pred", "load_pred"]])
