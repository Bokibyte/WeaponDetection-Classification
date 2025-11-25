from ultralytics import YOLO
from utils.organizer import Organizer
from utils.autocropper import autoCropper

def main():
    
    trainName = "classification/automaticRifle"
    model = YOLO("models/yolov8n.pt")

    model.train(
        data="datasets/gun_classification/structured/data.yaml",
        epochs=20,
        imgsz=448,
        batch=8,
        device=0,
        workers=1,
        mosaic=0,
        lr0=0.01,
        copy_paste=0,
        mixup=0,
        cache=True,

        save_dir= f"runs/{trainName}/train"
    )
    
    Organizer(trainName)
    autoCropper(trainName, "gun_classification/structured", trainName)

if __name__ == "__main__":
    main()
    
    
    
    
    
    
