import os
import glob
import shutil

class Organizer:
    def __init__(self, name):
        self.makeFolder = ["curve", "train", "val", "result"]
        self.loadPath = "runs/detect/train"
        self.movePath = f"runs/{name}/train"
        
    def organize(self):
        for folder in self.makeFolder:
            if folder == "curve":
                self.getFile = glob.glob(f"{self.loadPath}/*curve*")
                
                os.makedirs(f"{self.loadPath}/{folder}", exist_ok=True)
                [shutil.move(file, f"{self.loadPath}/{folder}") for file in self.getFile]
            elif folder == "result":
                self.getFile = glob.glob(f"{self.loadPath}/result*") + [f"{self.loadPath}/labels.jpg"]
                self.getFile.extend(glob.glob(f"{self.loadPath}/*matrix*")) 
                
                os.makedirs(f"{self.loadPath}/{folder}", exist_ok=True)
                [shutil.move(file, f"{self.loadPath}/{folder}") for file in self.getFile]
            else:
                self.getFile = glob.glob(f"{self.loadPath}/{folder}*")
                
                os.makedirs(f"{self.loadPath}/{folder}", exist_ok=True)
                [shutil.move(file, f"{self.loadPath}/{folder}") for file in self.getFile]
                
        shutil.move(f"{self.loadPath}", self.movePath)
        shutil.rmtree("runs/detect")
        
        
                
                