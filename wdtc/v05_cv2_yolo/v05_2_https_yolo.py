from ultralytics import YOLO
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv032.stream/playlist.m3u8")

# 2. 모델 로드
model = YOLO("yolo11n.pt")

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    
    # 모델 예측
    results = model(frame)
    
    # 바운딩 박스 및 분류 값 표시
    annotated_frame = results[0].plot()
    
    # 윈도우 창 설정
    cv2.namedWindow("HTTPS", cv2.WINDOW_AUTOSIZE)
    # cv2.namedWindow("HTTPS", cv2.WINDOW_KEEPRATIO)
    cv2.imshow("HTTPS", annotated_frame)
    
    # 'q' 키를 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Q키를 눌렀습니다.")
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()