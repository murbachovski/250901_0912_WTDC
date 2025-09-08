import threading
import cv2
from ultralytics import YOLO

# 모델과 영상 소스 정의
MODEL_NAMES = ["yolo11n.pt", "yolo11n-seg.pt"]
SOURCES = ["http://210.99.70.120:1935/live/cctv032.stream/playlist.m3u8", 0]  # 로컬 비디오, 0 = 웹캠

# ESC 키로 전체 종료를 제어할 이벤트
stop_event = threading.Event()

def run_tracker_in_thread(model_name, source, window_name):
    model = YOLO(model_name)
    results = model.track(source, stream=True)  # stream=True → 제너레이터

    for r in results:
        if stop_event.is_set():
            break
        frame = r.plot()  # 탐지 결과가 그려진 프레임
        cv2.imshow(window_name, frame)

        # ESC 키 종료 처리 (전체 스레드 종료)
        if cv2.waitKey(1) & 0xFF == 27:
            stop_event.set()
            break

    cv2.destroyWindow(window_name)

# 스레드 생성 및 실행
tracker_threads = []
for video_file, model_name in zip(SOURCES, MODEL_NAMES):
    window_name = f"Tracker - {model_name}"
    thread = threading.Thread(target=run_tracker_in_thread, args=(model_name, video_file, window_name))
    tracker_threads.append(thread)
    thread.start()

# 모든 스레드 종료 대기
for thread in tracker_threads:
    thread.join()

cv2.destroyAllWindows()
