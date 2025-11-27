import os
import shutil
import glob

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
            name = os.path.splitext(os.path.basename(img))[0]

            if self.prefix == "*":
                pass
            else:
                ext = os.path.splitext(img)[1]
                newImg = f"{self.classes}_{idx}{ext}"

                shutil.copy(img, f"{self.outputPath}/{self.classes}/{newImg}")
                print(f"[OK] Copied IMG: {newImg}")


