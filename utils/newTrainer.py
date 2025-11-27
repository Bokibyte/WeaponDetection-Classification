from ultralytics import YOLO

class YOLOTrainer:
    def __init__(self, model_path):
        self.model_path = model_path

    def train(self, dataPath,
              epochs=30, imgsz=448, batch=16,
              device=0, workers=2):
        
        model = YOLO(self.model_path)

        model.train(
            data = f"datasets/{dataPath}",  # JUSTRU INI YG BENAR
            epochs = epochs,
            imgsz = imgsz,
            batch = batch,
            device = device,
            workers = workers,

            # TRAINING TUNING
            optimizer = "AdamW",     # jauh lebih stabil utk klasifikasi
            lr0 = 0.0005,            # learning rate pas
            dropout = 0.1,           # mencegah overfit
            patience = 20,           # early stopping
        
            # AUGMENTATION 
            hsv_h = 0.01,
            hsv_s = 0.3,
            hsv_v = 0.3,
            fliplr = 0.5,
            scale = 0.2,
        )
