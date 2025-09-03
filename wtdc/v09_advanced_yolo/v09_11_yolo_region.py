from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("v09_advanced_yolo/input.mp4")

# 2. 특정 좌표 설정
region_points = {
    "region-01" : [(222, 156),(236, 871),(1520, 866),(1436, 171)]
}

# 3. 구역 객체 설정
region = solutions.RegionCounter(
    model="yolo11n.pt",
    show=True,
    conf=0.5,
    region=region_points
)

# 4. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    
    region_frame = region(frame)
    
# 5. 자원 해제
cap.release()
cv2.destroyAllWindows()