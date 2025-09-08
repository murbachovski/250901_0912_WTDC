from ultralytics import YOLO


# Load a model
model = YOLO("yolov8n.pt")

# Export the model to OpenVINO format
model.export(format="openvino", half=True)  # Export with FP16 precision


# 1. PyTorch YOLOv8 모델 로드
model = YOLO("yolov8n.pt")

# 2. OpenVINO 포맷으로 INT8 양자화(export)
model.export(format="openvino", int8=True, dynamic=True)

# 옵션 설명:
# format="openvino"  -> OpenVINO IR 모델로 변환
# int8=True           -> INT8 양자화 적용
# dynamic=True        -> 입력 크기 동적 지원