from ultralytics import YOLO

model = YOLO("yolov8n.yaml")

results = model.train(data="config.yaml", epochs=60, imgsz=(640, 300))

