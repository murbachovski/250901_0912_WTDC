import threading
import cv2
import numpy as np
from ultralytics import YOLO

MODEL_NAMES = ["yolo11n.pt", "yolo11n-seg.pt"]
SOURCES = ["http://210.99.70.120:1935/live/cctv032.stream/playlist.m3u8", 0]  # HLS 스트림 + 웹캠

# ESC 키로 전체 종료 이벤트
stop_event = threading.Event()

# 두 모델 프레임을 저장할 버퍼
frames = [None, None]
lock = threading.Lock()

def run_tracker_in_thread(model_index, model_name, source):
    model = YOLO(model_name)
    results = model.track(source, stream=True)

    for r in results:
        if stop_event.is_set():
            break

        frame = r.plot()

        # 크기 표준화 (640x480)
        frame = cv2.resize(frame, (640, 480))

        # 공유 버퍼에 프레임 저장
        with lock:
            frames[model_index] = frame

        # ESC 체크
        if cv2.waitKey(1) & 0xFF == 27:
            stop_event.set()
            break

# 스레드 시작
tracker_threads = []
for i, (video_file, model_name) in enumerate(zip(SOURCES, MODEL_NAMES)):
    thread = threading.Thread(target=run_tracker_in_thread, args=(i, model_name, video_file))
    tracker_threads.append(thread)
    thread.start()

# 메인 루프: 하나의 창에서 두 영상 병합
while not stop_event.is_set():
    with lock:
        if frames[0] is not None and frames[1] is not None:
            combined = cv2.hconcat(frames)  # 좌우 결합
            cv2.imshow("Combined View", combined)

    if cv2.waitKey(1) & 0xFF == 27:
        stop_event.set()
        break

# 스레드 종료 대기
for thread in tracker_threads:
    thread.join()

cv2.destroyAllWindows()
