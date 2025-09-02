from sahi.predict import get_sliced_prediction
from sahi import AutoDetectionModel

# 1. 모델 경로 설정
model_path = "yolo11n.pt"

# 2. 모델 로드
detection_model = AutoDetectionModel.from_pretrained(
    model_type="ultralytics",
    model_path=model_path,
    confidence_threshold=0.4
)

# 3. 모델 예측(sahi 적용)
results = get_sliced_prediction(
    "demo_data/small-vehicles1.jpeg",
    detection_model,
    slice_height=200,
    slice_width=200,
    overlap_height_ratio=0.1,
    overlap_width_ratio=0.1
)

# 4. 모델 결과 저장
results.export_visuals(export_dir="sahi/slice/slice.jpg")
print("SAHI_SUCCESS")