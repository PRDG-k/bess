import streamlit as st
import pandas as pd
import asyncio
import websockets
import json
from datetime import datetime, timedelta

st.title("태양광 ESS 대시보드")

# 웹소켓을 통해 실시간 데이터 수신 (한 번에 한 데이터만 반환)
async def fetch_data():
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        # 서버에서 여러 메시지를 보낼 수 있지만, 여기서는 첫 메시지만 반환
        data = await websocket.recv()
        return json.loads(data)


# 데이터 리스트 초기화
if "pv" not in st.session_state:
    st.session_state["pv"] = []

    try:
        new_data = asyncio.run(fetch_data())
        # new_data에 "time" 필드가 "YYYY-MM-DD HH:MM:SS" 형식으로 있다고 가정
        st.session_state["pv"].append(new_data)

        # 현재 시각 기준으로 최근 24시간 이내 데이터만 유지
        now = datetime.now()
        filtered_data = []
        for d in st.session_state["pv"]:
            # 문자열을 datetime 객체로 변환
            data_time = datetime.strptime(d["time"], "%Y-%m-%d %H:%M:%S")
            if data_time >= now - timedelta(hours=24):
                filtered_data.append(d)
        st.session_state["pv"] = filtered_data
    except Exception as e:
        st.error(f"데이터 업데이트 중 오류 발생: {e}")


# 데이터 업데이트 버튼을 눌렀을 때 새 데이터를 받아서 리스트에 추가
if st.button("데이터 업데이트"):
    try:
        new_data = asyncio.run(fetch_data())
        # new_data에 "time" 필드가 "YYYY-MM-DD HH:MM:SS" 형식으로 있다고 가정
        st.session_state["pv"].append(new_data)

        # 현재 시각 기준으로 최근 24시간 이내 데이터만 유지
        now = datetime.now()
        filtered_data = []
        for d in st.session_state["pv"]:
            # 문자열을 datetime 객체로 변환
            data_time = datetime.strptime(d["time"], "%Y-%m-%d %H:%M:%S")
            if data_time >= now - timedelta(hours=24):
                filtered_data.append(d)
        st.session_state["pv"] = filtered_data
    except Exception as e:
        st.error(f"데이터 업데이트 중 오류 발생: {e}")

# 누적된 데이터가 있으면 DataFrame 생성 및 시각화
if st.session_state["pv"]:
    # DataFrame 생성 전에 "time" 컬럼을 datetime 형식으로 변환
    df = pd.DataFrame(st.session_state["pv"])
    df["time"] = pd.to_datetime(df["time"], format="%Y-%m-%d %H:%M:%S")
    # 시간순 정렬 (필요한 경우)
    df = df.sort_values("time")
    
    st.write("최근 24시간 데이터", df)
    # 인덱스를 time으로 설정한 후 차트 그리기
    st.line_chart(df.set_index("time")[["solar_pred", "load_pred"]])
else:
    st.write("현재 저장된 데이터가 없습니다. '데이터 업데이트' 버튼을 눌러 데이터를 수집하세요.")
