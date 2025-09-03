from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("v09_advanced_yolo/vehicle.mp4")

# 2. 비디오 정보
w, h, fps = (int(cap.get(i)) for i in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# 3. 비디오 저장
video_writer = cv2.VideoWriter(
    "yolo_speed.avi",
    cv2.VideoWriter_fourcc(*"MJPG"),
    fps,
    (w, h)
)

# 4. 스피드 라인 설정
speed_line = [(147, 308), (498, 304)]

# 5. 스피드 객체 설정
speed_estimator = solutions.SpeedEstimator(
    model="yolo11n.pt",
    show=True,
    region=speed_line,
    line_width=5
)

# 6. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    re_frame = cv2.resize(frame, (640, 480))
    
    speed_frame = speed_estimator(re_frame)
    
    video_writer.write(speed_frame.plot_im)
    
    cv2.waitKey(1)
    
# 7. 자원 해제
video_writer.release()
cap.release()
cv2.destroyAllWindows()