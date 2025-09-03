from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("v09_advanced_yolo/vehicles.mp4")

# 2. 비디오 정보
w, h, fps = (int(cap.get(i)) for i in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# 3. 비디오 저장
video_writer = cv2.VideoWriter(
    "yolo_speed.avi",
    cv2.VideoWriter_fourcc(*"MJPG"),
    fps,
    (64, 480)
)

# 2. 라인 설정
lines = [(54, 256), (584, 245)]

# 3. 객체 생성
count_lines = solutions.ObjectCounter(
    model="yolo11n.pt",
    show=True,
    region=lines
)

# 4. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    
    frame = cv2.resize(frame, (640, 480))
    count_frame = count_lines(frame)
    
# 5. 자원 해제
cap.release()
cv2.destroyAllWindows()
