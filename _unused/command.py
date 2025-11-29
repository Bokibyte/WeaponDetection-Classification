from utils.preprocessing import preprocess as prep
from utils.organizer import Organizer
from utils.trainer import YOLOTrainer
from utils.imageUtilities import checkImage
import os
import glob
import random
import shutil


weapClass = ["automatic_rifle", "bazooka", "grenade_launcher", "handgun", "knife", "shotgun", "smg", "sniper", "sword"]
yoloModel = "models/yolov8n-cls.pt"
testDataset = "datasets/testing"

def runTrain():
    for classes in weapClass:
        YOLOTrainer(yoloModel).train(f"gun_classification/{classes}")
        Organizer(f"classification/{classes}").organize()

def runPrep():
    for classes in weapClass:
        p = prep(f"gun_classification/_unstructured", f"gun_classification", classes)
        p.yamlGen()
        p.fixLabels()

def isWeapon():
    chkimg = checkImage()
    imgFiles = glob.glob(f"{testDataset}/*")
    [chkimg.isWeap(f) for f in imgFiles]
        
def imageClazzy():
    chkimg = checkImage()
    imgFiles = glob.glob("test/weapon/_crops/*")
    
    for img in imgFiles:
        scores = chkimg.runParallel(img, weapClass)

        imgName = os.path.splitext(os.path.basename(img))[0]   
        best_idx = scores.index(max(scores))

        bestClass = weapClass[best_idx]
        bestScore = scores[best_idx]
        print(f"[{imgName}] terbaik:", bestClass, bestScore)

        originalName = imgName.split("_crop_")[0] + ".jpg"

        os.makedirs(f"test/weapon/{bestClass}", exist_ok=True)

        shutil.copy(
            f"test/weapon/_raw/{originalName}",
            f"test/weapon/{bestClass}"
        )


if __name__ == "__main__":
    runTrain()

