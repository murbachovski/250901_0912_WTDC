import streamlit as st
from ultralytics import YOLO
import cv2

import pandas as pd
import plotly.express as px
import time

# 1. 페이지 기본 설정
st.set_page_config(layout="wide")
st.title("Streamlit을 이용한 YOLO 웹 사이트")

# 2. 화면 설정
col1, col2 = st.columns(2)

with col1:
    frame_placeholder = st.empty()

with col2:
    chart_placeholder = st.empty()

# 3. 비디오 경로 설정
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv032.stream/playlist.m3u8")

# 4. 모델 로드
model = YOLO("yolo11n.pt")

# 5. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        st.warning("CCTV ERROR")
        break
    
    results = model(frame)
    
    annotated_frame = results[0].plot()
    
    labels = [model.names[int(c)] for c in results[0].boxes.cls]
    
    # names_list = []
    # for c in results[0].boxes.cls:  # 각 탐지된 객체의 클래스 ID 순회
    #     class_id = int(c)           # 텐서를 정수로 변환
    #     class_name = model.names[class_id]  # 모델에서 이름 가져오기
    #     names_list.append(class_name)
    
    if labels:
        # 리스트를 데이터프레임으로 변환 후 개수 집계
        df_count = pd.DataFrame({"Object": labels})
        df_count = df_count.value_counts().reset_index(name="Count")
        
        # px를 사용해서 막대 그래프 생성
        fig = px.bar(
            df_count,
            x="Object",
            y="Count",
            title="탐지 객체 수",
            color="Object",
            text="Count"
        )
        fig.update_layout(showlegend=False)
        fig.update_traces(textposition="outside")
    else:
        df_count = pd.DataFrame({"Object": [], "Count": []})
        fig = px.bar(
            df_count,
            x="Object",
            y="Count",
            title="탐지 객체 수"
        )
    
    frame_placeholder.image(annotated_frame, channels="BGR")
    chart_placeholder.plotly_chart(fig, use_container_width=True, key=f"chart_{time.time()}")
    
# 6. 자원 해제
cap.release()
cv2.destroyAllWindows()