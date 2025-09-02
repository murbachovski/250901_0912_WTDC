from ultralytics import YOLO
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv046.stream/playlist.m3u8")

# 2. 모델 로드
model = YOLO("yolo11s.pt")

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    
    # YOLO 객체 탐지
    results = model(frame)
    
    # 바운딩 박스 및 클래스 표시
    annotated_frame = results[0].plot()
    
    # 탐지된 객체 정보
    boxes = results[0].boxes
    
    # 탐지된 객체 수 계산
    count = 0
    for i in boxes.cls:
        count += 1
    
    # 조건문으로 상태 메시지 결정
    if count >= 10:
        status = "Danger"
        color = (0, 0, 255)
    elif count >= 7:
        status = "Warning"
        color = (0, 255, 0)
    elif count >= 3:
        status = "Normal"
        color = (0, 0, 0)
    else:
        status = "Safe"
        color = (255, 0, 0)
        
    # 화면에 탐지된 객체 수 표시
    cv2.putText(
        annotated_frame, # 표시 프레임
        f"Detected : {count}, {status}", # 표시 내용
        (10, 30), # 좌측 상단 위치
        cv2.FONT_HERSHEY_SIMPLEX, # 폰트 스타일
        1, # 폰트 크기
        # (0, 0, 255), # 글자색
        color,
        2, # 두께
        cv2.LINE_AA # 안티앨리어싱 적용
    )
    
    # 결과 영상 출력
    cv2.namedWindow("PUT_TEXT", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("PUT_TEXT", annotated_frame)
    
    # 'q' 키를 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q 키를 눌러서 종료했습니다.")
        break
# 자원 해제
cap.release()
cv2.destroyAllWindows()