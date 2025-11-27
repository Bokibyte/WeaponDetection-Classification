from ultralytics import YOLO

class YOLOTrainer:
    def __init__(self, model_path):
        self.model_path = model_path

    def train(self, dataPath,
              epochs=20, imgsz=448, batch=8,
              device=0, workers=1):
        
        model = YOLO(self.model_path)

        model.train(
            data = f"datasets/{dataPath}/data.yaml",
            epochs = epochs,
            imgsz = imgsz,
            batch = batch,
            device = device,
            workers = workers,
            mosaic = 0,
            lr0 = 0.01,
            copy_paste = 0,
            mixup = 0,
            cache = True,
        )