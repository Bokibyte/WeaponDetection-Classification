from utils.Preprocessing import preprocess as prep
from utils.Preprocessing import cropBatch
from utils.Trainer import YOLOTrainer
from utils.Organizer import Organizer
from utils.ImageUtilities import checkImage
from ultralytics import YOLO
import os
import shutil
import glob

weapClass = ["automatic_rifle", "bazooka", "grenade_launcher", "handgun", "knife", "shotgun", "smg", "sniper", "sword"]
yoloModel = "models/yolov8s-cls.pt"
yoloDetection = YOLO("runs/detection/train/weights/best.pt")
yoloClassification = YOLO("runs/classification/train/weights/best.pt")

testDataset = "datasets/testing"
chkImg = checkImage(weapClass)


def nwPrep():
    for classes in weapClass:
        p = prep(f"_unstructured", f"gun_classification", classes)
        p.createFolder()
        p.copyFile()
        
def runTrain():
    YOLOTrainer(yoloModel).train(f"gun_classification_cropped")

def isWeapon():
    imgFiles = glob.glob(f"{testDataset}/*")
    [chkImg.isWeap(f) for f in imgFiles]

def imageClazzy():
    for img in glob.glob("test/weapon/_crops/*"):
        nameImg = os.path.splitext(os.path.basename(img))[0]
        best, score, _ = chkImg.getBest(img)
        chkImg.saveToFolder(img)
        print (f"[DONE] ({nameImg}) Class: {best}, Score: {score}")
    
def organize():
    shutil.rmtree("runs/classification/train")
    Organizer("classify","classification").organize()
    
def cropTs():
    for clazz in weapClass:
        cropBatch("gun_classification", clazz, yoloDetection, padding=30)


if __name__ == "__main__":
    runTrain()
    organize()