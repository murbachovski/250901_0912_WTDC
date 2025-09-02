import cv2
from ultralytics import YOLO
from v08_3_cctv_its import its_cctv

# 1. 비디오 경로 설정
test_url = its_cctv()
cap = cv2.VideoCapture(test_url)

# 2. 모델 로드
model = YOLO("yolo11n.pt")

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    results = model(frame)
    annotated_frame = results[0].plot()
    
    # 윈도우 설정
    cv2.namedWindow("ITS_YOLO", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("ITS_YOLO", annotated_frame)
    
    # q키를 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
       print("Q키를 눌러서 종료했습니다.")
       break
   
# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()