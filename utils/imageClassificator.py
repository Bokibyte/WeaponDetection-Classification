from ultralytics import YOLO
import os
import shutil

class checkImage:
    def __init__(self):
        self.detectionModel = "runs/detection/train/weights/best.pt"
        
    def isWeap(self, img):
        self.image = img
        self.coef = 0
        self.imgName = os.path.splitext(os.path.basename(self.image))[0]
        self.checkImg = self.detectionModel(self.image, verbose=False)
        boxes = self.checkImg[0].boxes
        
        if boxes is None or len(boxes) == 0:
            self.coef = 0.0
            shutil.copy(self.image, "test/not_weapon")
            print(f"[DONE] img {self.imgName} isnt a weapon.")
        else:
            self.coef = float(boxes.conf.max().cpu().numpy())
            shutil.copy(self.image, "test/weapon/raw")
            print(f"[DONE] img {self.imgName} is a weapon.")
        
        print(f"[DONE] img {self.imgName} had coef: {self.coef}")
        return self.coef
        
    def getCoef(self, img, modelPath, classes):
        self.model = f"{modelPath}/best.pt"
        self.image = img
        self.cls = classes
        self.coef = 0

        self.checkImg = self.detectionModel(self.image, verbose=False)
        boxes = self.checkImg[0].boxes
        
        if boxes is None or len(boxes) == 0:
            self.coef = 0.0
        else:
            self.coef = float(boxes.conf.max().cpu().numpy())
            
        return self.coef
        
        
    