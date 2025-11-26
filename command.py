from utils.preprocessing import preprocess as prep
from utils.organizer import Organizer
from utils.trainer import YOLOTrainer
from utils.imageUtilities import checkImage
import os
import glob
import random
import shutil


weapClass = ["automatic_rifle", "bazooka", "grenade_launcher", "handgun", "knife", "shotgun", "smg", "sniper", "sword"]
yoloModel = "models/yolov8n.pt"
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
    imgFiles = glob.glob(f"{testDataset}*")
    [chkimg.isWeap(f) for f in imgFiles]
        
def imageClazzy5():
    chkimg = checkImage()
    imgFiles = random.sample(glob.glob("test/weapon/_crops/*"),5)
    
    for img in imgFiles:
        scores = chkimg.runParallel(img, weapClass)
        
        imgName = os.path.splitext(os.path.basename(img))[0]
        best_idx = scores.index(max(scores))
        print(f"[{imgName}] terbaik:", weapClass[best_idx], scores[best_idx])
        
        os.makedirs(f"test/weapon/{weapClass[best_idx]}", exist_ok=True)
        shutil.copy(f"test/weapon/_raw/{os.path.basename(img)}", f"test/weapon/{weapClass[best_idx]}")

if __name__ == "__main__":
    isWeapon()
    imageClazzy5()
