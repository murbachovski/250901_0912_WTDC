import cv2
import time
from ultralytics import YOLO

# -------------------------------
# 1. 모델 로드
# -------------------------------
model = YOLO("yolov8n_int8_openvino_model")  # PyTorch YOLOv8
# yolo11n.pt => 13
# yolov8n.pt => 13
# yolov8n_openvino_model_ => 10
# yolov8n_int8_openvino_model => 20

# -------------------------------
# 2. 영상 소스 설정
# -------------------------------
# 웹캠: 0, HLS 스트림 등 URL 가능
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv032.stream/playlist.m3u8")

# -------------------------------
# 3. FPS 측정용 변수
# -------------------------------
fps = 0
alpha = 0.9  # EMA 스무딩
prev_time = time.time()

# -------------------------------
# 4. 실시간 추론 루프
# -------------------------------
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # -------------------------------
    # 4-1. 모델 추론
    # -------------------------------
    start = time.time()
    results = model(frame)  # 단일 프레임 탐지
    end = time.time()

    # -------------------------------
    # 4-2. FPS 계산
    # -------------------------------
    curr_fps = 1 / (end - start) if (end - start) > 0 else 0
    fps = alpha * fps + (1 - alpha) * curr_fps

    # -------------------------------
    # 4-3. 결과 시각화
    # -------------------------------
    frame = results[0].plot()
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # -------------------------------
    # 4-4. 출력
    # -------------------------------
    cv2.imshow("YOLOv8 Real-time Detection", frame)

    # ESC 키로 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break

# -------------------------------
# 5. 종료
# -------------------------------
cap.release()
cv2.destroyAllWindows()
