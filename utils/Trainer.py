from ultralytics import YOLO

class YOLOTrainer:
    def __init__(self, modelPath):
        self.modelPath = modelPath

    def train(self, dataPath,
              epochs=30, imgsz=448, batch=16,
              device=0, workers=2):
        
        model = YOLO(self.modelPath)

        model.train(
            data = f"datasets/{dataPath}", 
            epochs = epochs,
            imgsz = imgsz,
            batch = batch,
            device = device,
            workers = workers,

            # TRAINING TUNING
            optimizer = "AdamW",    
            lr0 = 0.0005,           
            dropout = 0.1,          
            patience = 20,          
        
            # AUGMENTATION 
            hsv_h = 0.01,
            hsv_s = 0.3,
            hsv_v = 0.3,
            fliplr = 0.5,
            scale = 0.2,
        )
