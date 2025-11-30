from concurrent.futures import ThreadPoolExecutor
from ultralytics import YOLO
import os
import shutil
import cv2

class checkImage:
    def __init__(self, cls):

        
        self.classes = cls 


    def isWeap(self, img):
        self.detectionModel = YOLO("runs/detection/train/weights/best.pt")
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

        os.makedirs("test/weapon/_raw", exist_ok=True)
        ext = os.path.splitext(self.image)[1]
        shutil.copy(self.image, f"test/weapon/_raw/{self.imgName}{ext}")

        print(f"[DONE] img {self.imgName} is a weapon.")
        print(f"[DONE] img {self.imgName} had coef: {self.coef}")

        imgCv = cv2.imread(self.image)
        cropSave = f"test/weapon/_crops"
        os.makedirs(cropSave, exist_ok=True)

        counter = 0
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            crop = imgCv[y1:y2, x1:x2]

            savePath = os.path.join(cropSave, f"{self.imgName}_{counter}.jpg")

            cv2.imwrite(savePath, crop)
            print(f"[CROP] Saved: {savePath}")
            counter += 1

        return self.coef


    def getScores(self, img):
        self.classifyModel  = YOLO("runs/classification/train/weights/best.pt")
        result = self.classifyModel(img, verbose=False)[0]

        if result.probs is None:
            return []

        return result.probs.data.cpu().numpy().tolist()
    def getBest(self, img):

        scores = self.getScores(img)
        if not scores:
            return None, 0.0, []

    def getBest(self, img):

        "Mengembalikan (kelas_terbaik, score_terbaik, list_scores)"
        scores = self.getScores(img)
        if not scores:
            return None, 0.0, []
        best_idx = scores.index(max(scores))
        best_class = self.classes[best_idx]
        best_score = scores[best_idx]

        return best_class, best_score, scores
    
    def saveToFolder(self, img):
        
        dstRoot ="test/weapon/"
        os.makedirs(dstRoot, exist_ok=True)
        best_class, best_score, _ = self.getBest(img)
        if best_class is None:
            print(f"[SKIP] {img} tidak bisa diklasifikasi.")
            return

        os.makedirs(f"{dstRoot}/{best_class}", exist_ok=True)

        shutil.copy(img, f"{dstRoot}/{best_class}/")
        print(f"[OK] {os.path.basename(img)} → {best_class} ({best_score:.3f})")