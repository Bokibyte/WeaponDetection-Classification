from utils.preprocessing import preprocess as prep
from utils.organizer import Organizer
from utils.trainer import YOLOTrainer
from utils.imageClassificator import checkImage
from concurrent.futures import ThreadPoolExecutor
import glob
import random


weapClass = ["automatic_rifle", "bazooka", "grenade_launcher", "handgun", "knife", "shotgun", "smg", "sniper", "sword"]
yoloModel = "models/yolov8n.pt"
testDataset = ""

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
        
def imageClazzy(img, model, classes):
    imgCoef = []
    imgFiles = random.sample(glob.glob("crops/detection/*"),5)
    chkimg = checkImage()
    chkimg.getCoef(img, model, classes)
    

        
if __name__ == "__main__":
    runTrain()