import os
import glob
import shutil

class Organizer:
    def __init__(self, inputPath, movePath):
        self.makeFolder = ["curve", "train", "val", "result"]
        self.loadPath   = f"runs/{inputPath}/train"
        self.movePath   = f"runs/{movePath}/train"

    def organize(self):
        
        if not os.path.exists(self.loadPath):
            print(f"[ERR] Folder not found: {self.loadPath}")
            return
        
        for folder in self.makeFolder:

            dst = f"{self.loadPath}/{folder}"
            os.makedirs(dst, exist_ok=True)

            if folder == "curve":
                self.getFile = glob.glob(f"{self.loadPath}/*curve*")

            elif folder == "result":
                self.getFile  = glob.glob(f"{self.loadPath}/results*")
                self.getFile += glob.glob(f"{self.loadPath}/*matrix*")
                self.getFile += glob.glob(f"{self.loadPath}/labels.jpg")

            else:  
                self.getFile = glob.glob(f"{self.loadPath}/{folder}*")

            for file in self.getFile:
                if os.path.exists(file):
                    try:
                        shutil.move(file, dst)
                        print(f"[MOVE] {file} → {dst}")
                    except:
                        pass

        os.makedirs(os.path.dirname(self.movePath), exist_ok=True)

        shutil.move(self.loadPath, self.movePath)

        if os.path.exists(self.loadPath):
            shutil.rmtree(self.loadPath)

        print(f"[DONE] Organized to: {self.movePath}")
