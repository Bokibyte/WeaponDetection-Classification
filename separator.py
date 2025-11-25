import os
import shutil
import glob
from concurrent.futures import ThreadPoolExecutor

mainPath = "datasets/gun_classification"

weapClass = ["automatic_rifle", "rocket_launcher", "grenade_launcher", "handgun", "knife", "shotgun", "smg", "sniper", "sword"]

for classes in weapClass:
    os.makedirs(f"{mainPath}/{classes}", exist_ok=True)

def toImages(weapClass):
    trainSrc = os.path.join(mainPath, "images", "train")
    valSrc   = os.path.join(mainPath, "images", "val")

    dstTrain = os.path.join(mainPath, weapClass, "images", "train")
    dstVal   = os.path.join(mainPath, weapClass, "images",  "val")

    os.makedirs(dstTrain, exist_ok=True)
    os.makedirs(dstVal, exist_ok=True)

    prefix = f"{weapClass[:3]}*"

    filesTrain = glob.glob(os.path.join(trainSrc, prefix))
    filesVal   = glob.glob(os.path.join(valSrc, prefix))

    for idx, f in enumerate(filesTrain):
        ext = os.path.splitext(f)[1]
        newname = f"{weapClass}_train_{idx}{ext}"
        shutil.copy(f, os.path.join(dstTrain, newname))
        print(f"[DONE] train: Copied IMG → {newname}")

    for idx, f in enumerate(filesVal):
        ext = os.path.splitext(f)[1]
        newname = f"{weapClass}_val_{idx}{ext}"
        shutil.copy(f, os.path.join(dstVal, newname))
        print(f"[DONE] val: Copied IMG → {newname}")


    
def toLabels(weapClass):
    trainSrc = os.path.join(mainPath, "labels", "train")
    valSrc   = os.path.join(mainPath, "labels", "val")

    dstTrain = os.path.join(mainPath, weapClass, "labels", "train")
    dstVal   = os.path.join(mainPath, weapClass, "labels",  "val")

    os.makedirs(dstTrain, exist_ok=True)
    os.makedirs(dstVal, exist_ok=True)

    prefix = f"{weapClass[:3]}*"

    filesTrain = glob.glob(os.path.join(trainSrc, prefix))
    filesVal   = glob.glob(os.path.join(valSrc, prefix))

    for idx, f in enumerate(filesTrain):
        newname = f"{weapClass}_train_{idx}.txt"
        shutil.copy(f, os.path.join(dstTrain, newname))
        print(f"[DONE] train: Copied TXT → {newname}")

    for idx, f in enumerate(filesVal):
        newname = f"{weapClass}_val_{idx}.txt"
        shutil.copy(f, os.path.join(dstVal, newname))
        print(f"[DONE] val: Copied TXT → {newname}")

def runCopyTrain():
    for classes in weapClass:
        toImages(classes)
        
def runCopyVal():
    for classes in weapClass:
        toLabels(classes)

with ThreadPoolExecutor(max_workers=2) as exe:
    exe.submit(runCopyTrain)
    exe.submit(runCopyVal)