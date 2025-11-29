from ultralytics import YOLO

def main():
    model = YOLO("models/yolov8n.pt")

    model.train(
        data="datasets/gun_detection/data.yaml",
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
    )

if __name__ == "__main__":
    main()
