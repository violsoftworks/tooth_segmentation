from ultralytics import YOLO
import torch
import multiprocessing

torch.cuda.set_device(0) 

def train_model():
    model = YOLO('yolov8n-seg.pt') 
    results = model.train(data='config_seg.yaml', batch=8, epochs=200)


if __name__ == "__main__":
    train_model()

