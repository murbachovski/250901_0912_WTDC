from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("v09_advanced_yolo/input_distance.mp4")

# 2. 거리 계산 객체 생성
distance_calculator = solutions.DistanceCalculation(
    model="yolo11n.pt",
    show=True
)

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    
    results = distance_calculator(frame)
    
# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()