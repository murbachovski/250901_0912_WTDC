from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("v09_advanced_yolo/input.mp4")

# 2. Heatmap 설정
heatmap = solutions.Heatmap(
    model="yolo11n.pt",
    show=True,
    conf=0.1,
    colormap=cv2.COLORMAP_PARULA
    # colormap=cv2.COLORMAP_JET
)
# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    
    heat_frame = heatmap(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q키를 눌러서 종료합니다.")
        break
        
# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()