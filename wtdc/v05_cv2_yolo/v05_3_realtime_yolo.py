from ultralytics import YOLO
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture(0)

# 2. 모델 로드
model = YOLO("yolo11n.pt")

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    
    # 모델 객체 탐지 수행
    results = model(frame)
    
    # 바운딩 박스 및 라벨 표시
    annotated_frame = results[0].plot()
    
    # 윈도우 창 설정
    cv2.imshow("REALTIME", annotated_frame)
    
    # q키를 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q키를 눌러서 종료")
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
        