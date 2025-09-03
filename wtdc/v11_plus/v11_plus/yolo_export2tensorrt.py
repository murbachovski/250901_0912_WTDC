from ultralytics import YOLO

model = YOLO("yolo11n.pt")
model.export(format="engine")  # creates 'yolo11n.engine'

# Run inference
model = YOLO("yolo11n.engine")
results = model("https://ultralytics.com/images/bus.jpg")