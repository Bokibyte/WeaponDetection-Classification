import os
import shutil
import glob
import cv2

class preprocess():
    def __init__(self, inputPath, outputPath, classes):
        
        self.classes = classes
        self.name = inputPath
        self.inputPath = f"datasets/{inputPath}"
        self.outputPath = f"datasets/{outputPath}"

        if not self.classes:
            self.prefix = "*"
        else:
            self.prefix = f"{self.classes[:3]}*" 

    def createFolder(self):
        if self.prefix == "*":
            pass
        else:
            os.makedirs(f"{self.outputPath}/{self.classes}", exist_ok=True)

    def copyFile(self):
        self.getImg = (
            glob.glob(f"{self.inputPath}/train/images/{self.prefix}") +
            glob.glob(f"{self.inputPath}/val/images/{self.prefix}")
        )

        for idx, img in enumerate(self.getImg):

            if self.prefix == "*":
                pass
            else:
                ext = os.path.splitext(img)[1]
                newImg = f"{self.classes}_{idx}{ext}"

                shutil.copy(img, f"{self.outputPath}/{self.classes}/{newImg}")
                print(f"[OK] Copied IMG: {newImg}")

class cropBatch():
    def __init__(self, datasetsName, className, modelPath, padding):
        self.etcF = ["train", "val"]
        self.model = modelPath
        
        for f in self.etcF:
            self.workinDir = f"datasets/{datasetsName}/{f}/{className}"
            getImg = glob.glob(f"{self.workinDir}/*")
            for images in getImg:
                imgName = os.path.splitext(os.path.basename(images))[0]
                img = cv2.imread(images)

                if img is None:
                    print(f"[SKIP] cant read: {images}")
                    continue

                h, w = img.shape[:2]

                result = self.model(images, verbose=False)[0]
                boxes = result.boxes

                if boxes is None or len(boxes) == 0:
                    print(f"[NO WEAPON] {images}")
                    continue

                saveFolder = f"datasets/{datasetsName}_cropped/{f}/{className}"
                os.makedirs(saveFolder, exist_ok=True)

                counter = 0
                for box in boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    x1 = max(0, x1 - padding)
                    y1 = max(0, y1 - padding)
                    x2 = min(w, x2 + padding)
                    y2 = min(h, y2 + padding)

                    crop = img[y1:y2, x1:x2]

                    savePath = f"{saveFolder}/{imgName}_{counter}.jpg"
                    cv2.imwrite(savePath, crop)

                    print(f"[CROP] {imgName} saved: {savePath}")
                    counter += 1

            print("\n[DONE] Auto-crop datasets")