from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv032.stream/playlist.m3u8")

# 2. 객체 생성
cropper = solutions.ObjectCropper(
    model="yolo11n.pt",
    show=False,
    conf=0.7,
    classes=[0, 2]
)

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    
    crop_frame = cropper(frame)
    cv2.imshow("CROP", crop_frame.plot_im)
    # 250903 결과 영상 출력 연구
    cv2.waitKey(30)
    
# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()