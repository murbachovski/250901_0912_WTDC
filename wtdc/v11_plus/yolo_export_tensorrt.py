from ultralytics import YOLO

# Load a model
model = YOLO('yolo11l.pt')

# Export the model
# model.export(format='engine', device=0, int8=True)
model.export(format='engine', device=0)