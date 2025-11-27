from utils.newPreprocessing import preprocess as prep
from utils.newTrainer import YOLOTrainer
from utils.newOrganizer import Organizer
from utils.newImageUtilities import checkImage
import os
import shutil
import glob

weapClass = ["automatic_rifle", "bazooka", "grenade_launcher", "handgun", "knife", "shotgun", "smg", "sniper", "sword"]
yoloModel = "models/yolov8s-cls.pt"
testDataset = "datasets/testing"

def nwPrep():
    for classes in weapClass:
        p = prep(f"_unstructured", f"gun_classification", classes)
        p.createFolder()
        p.copyFile()
        
def runTrain():
    YOLOTrainer(yoloModel).train(f"gun_classification")

def isWeapon():
    chkimg = checkImage()
    imgFiles = glob.glob(f"{testDataset}/*")
    [chkimg.isWeap(f) for f in imgFiles]

def imageClazzy():
    chkImg = checkImage(weapClass)
    for img in glob.glob("test/weapon/_crops/*"):
        nameImg = os.path.splitext(os.path.basename(img))[0]
        best, score, _ = chkImg.getBest(img)
        chkImg.saveToFolder(img)
        print (f"[DONE] ({nameImg}) Class: {best}, Score: {score}")
    

def organize():
    shutil.rmtree("runs/classification/train")
    Organizer("classify","classification").organize()

if __name__ == "__main__":
    imageClazzy()