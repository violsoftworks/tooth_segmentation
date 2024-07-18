from ultralytics import YOLO
import torch

torch.cuda.set_device(0) 
torch.cuda.empty_cache()

def train_model():
    model = YOLO('yolov8n-seg.pt') 
    model.train(data='full_teeth_config.yaml', batch=2, epochs=300, imgsz=800,
                conf=0.5, fliplr=0.0, flipud=0.0, hsv_h=1, hsv_v=1, hsv_s=0.8, translate=0,
                copy_paste=0, crop_fraction=0)


if __name__ == "__main__":
    train_model()

