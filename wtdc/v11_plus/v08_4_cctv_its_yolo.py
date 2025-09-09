import cv2
import time
from ultralytics import YOLO
from v08_openapi.v08_3_cctv_its import its_cctv

# 1. 비디오 경로 설정
test_url = its_cctv()
cap = cv2.VideoCapture(test_url)

# 2. 모델 로드 (TensorRT 엔진 사용)
model = YOLO("yolo11l.engine")
# 지난 10초 동안의 평균 FPS: 11.24
# 지난 10초 동안의 평균 FPS: 16.28
# 지난 10초 동안의 평균 FPS: 15.59
# 지난 10초 동안의 평균 FPS: 15.76
# 지난 10초 동안의 평균 FPS: 15.86

model = YOLO("yolo11n.engine")
# 지난 10초 동안의 평균 FPS: 31.65
# 지난 10초 동안의 평균 FPS: 39.42
# 지난 10초 동안의 평균 FPS: 39.99
# 지난 10초 동안의 평균 FPS: 39.52
# 지난 10초 동안의 평균 FPS: 39.98

# model = YOLO("yolo11n.pt")
# 지난 10초 동안의 평균 FPS: 23.79
# 지난 10초 동안의 평균 FPS: 31.71
# 지난 10초 동안의 평균 FPS: 32.24
# 지난 10초 동안의 평균 FPS: 31.63
# 지난 10초 동안의 평균 FPS: 31.77

# model = YOLO("yolo11n_int.engine")
# 지난 10초 동안의 평균 FPS: 27.39
# 지난 10초 동안의 평균 FPS: 54.07
# 지난 10초 동안의 평균 FPS: 59.58
# 지난 10초 동안의 평균 FPS: 38.25
# 지난 10초 동안의 평균 FPS: 34.16

# 3. FPS 계산을 위한 변수 초기화
total_frames = 0
total_time = 0.0
fps_start_time = time.time()
frame_count_for_avg = 0

# 4. 비디오 프레임 처리
while cap.isOpened():
    # 프레임 읽기
    success, frame = cap.read()
    if not success:
        print("프레임을 읽을 수 없거나, 비디오 파일의 끝입니다.")
        break
    
    # 실시간 FPS 측정을 위한 시작 시간
    frame_start_time = time.time()
    
    # 추론 실행
    results = model(frame, verbose=False, device=0, conf=0.3, iou=0.6, classes=[2])
    
    # 실시간 FPS 측정을 위한 종료 시간
    frame_end_time = time.time()
    
    # 실시간 FPS 계산
    realtime_fps = 1 / (frame_end_time - frame_start_time)
    
    # 평균 FPS 계산을 위한 누적
    total_frames += 1
    total_time += (frame_end_time - frame_start_time)
    frame_count_for_avg += 1
    
    # 10초마다 평균 FPS 출력
    current_time = time.time()
    if current_time - fps_start_time >= 10:
        avg_fps = frame_count_for_avg / (current_time - fps_start_time)
        print(f"지난 10초 동안의 평균 FPS: {avg_fps:.2f}")
        
        # 변수 초기화
        fps_start_time = current_time
        frame_count_for_avg = 0
    
    # 시각화
    annotated_frame = results[0].plot()
    
    # 화면에 FPS 표시 (변수명 수정)
    cv2.putText(annotated_frame, f"Realtime FPS: {realtime_fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    # 윈도우 표시
    cv2.namedWindow("ITS_YOLO", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("ITS_YOLO", annotated_frame)
    
    # 'q' 키를 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Q키를 눌러서 종료했습니다.")
        break
    
# 자원 해제
cap.release()
cv2.destroyAllWindows()