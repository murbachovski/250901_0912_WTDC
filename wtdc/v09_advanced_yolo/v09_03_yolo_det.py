from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolo11l.pt")

# 2. 모델 예측
results = model(
    "v09_advanced_yolo/test_input.jpg",
    save=True,
    # max_det=2, # 최대 감지 개수 설정
    # save_txt=True, # 텍스트로 결과 정보 저장
    # save_conf=True, # 탐지 신뢰도 값 저장
    # save_crop=True, # 탐지된 객체 이미지 저장
    # visualize=True
    classes=[41, 74]
)
# cup, clock만 예측 되게끔!!