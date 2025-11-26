from concurrent.futures import ThreadPoolExecutor
from ultralytics import YOLO
import os
import shutil
import cv2

class checkImage:
    def __init__(self):
        self.detectionModel = YOLO("runs/detection/train/weights/best.pt")
        
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
            print(f"[DONE] img {self.imgName} had coef: {self.coef}")
            return self.coef

        self.coef = float(boxes.conf.max().cpu().numpy())
        shutil.copy(self.image, "test/weapon/raw")
        print(f"[DONE] img {self.imgName} is a weapon.")
        print(f"[DONE] img {self.imgName} had coef: {self.coef}")
        
        imgCv = cv2.imread(self.image)
        crop_save_folder = f"test/weapon/crops/{self.imgName}"
        os.makedirs(crop_save_folder, exist_ok=True)
        
        counter = 0
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            crop = imgCv[y1:y2, x1:x2]

            savePath = os.path.join(crop_save_folder, f"{self.imgName}_crop_{counter}.jpg")
            cv2.imwrite(savePath, crop)

            print(f"[CROP] Saved: {savePath}")
            counter += 1
            
        return self.coef

    def getCoef(self, img, classes):
        self.model = YOLO(f"runs/classification/{classes}/weights//best.pt")
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
    
    def _wrapper(self, params):
        img, cls = params
        return self.getCoef(img, cls)

    def runParallel(self, img, classes):
        params = [(img, cls) for cls in classes]
        
        with ThreadPoolExecutor() as exec:
            result = list(exec.map(self._wrapper, params))
        return result
        
        
    