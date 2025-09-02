from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv008.stream/playlist.m3u8")

# 2. 이메일 인증 정보
from_email = "ai.murbachovski@gmail.com"
passwoard = "lzrj wuld nfob dhsa"
to_email = "ai.murbachovski@gmail.com"

# 3. 보안 알림 시스템 객체 생성
security = solutions.SecurityAlarm(
    model="yolo11n.pt",
    show=True,
    records=3 # 탐지된 객체 수가 record 수 이상일 때 이메일을 전송합니다.
)

# 4. 이메일 인증
security.authenticate(from_email, passwoard, to_email)

# 5. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 읽기 실패 및 종료")
        break
    
    # 객체 탐지 수행
    result_frame = security(frame)
    
    # ESC 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
# 6. 자원 해제
cap.release()
cv2.destroyAllWindows()

# pip install shapely
# pip install lap