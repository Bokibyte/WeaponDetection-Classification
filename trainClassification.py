from ultralytics import YOLO
from utils.organizer import Organizer

weapClass = ["automatic_rifle", "bazooka", "grenade_launcher", "handgun", "knife", "shotgun", "smg", "sniper", "sword"]  

def trainTs(cls, model):
    model = YOLO(f"models/{model}")
    model.train(
        data = f"datasets/gun_classification/{cls}/data.yaml",
        epochs = 20,
        imgsz = 448,
        batch = 8,
        device = 0,
        workers = 1,
        mosaic = 0,
        lr0 = 0.01,
        copy_paste = 0,
        mixup = 0,
        cache = True,
    )

if __name__ == '__main__':
    for cls in weapClass:
        trainTs(cls, "yolov8n.pt")
        Organizer(f"classification/{cls}")
        print(f"[DONE] Trained {cls}")