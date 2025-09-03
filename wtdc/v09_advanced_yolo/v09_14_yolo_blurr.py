from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture(0)

# 2. blurr 객체 생성
blurrer = solutions.ObjectBlurrer(
    model="yolo11n.pt",
    show=True,
    blur_ratio=0.7,
    classes=0
)

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    
    blur_frame = blurrer(frame)

# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()
