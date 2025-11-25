import os
import shutil
import glob
from concurrent.futures import ThreadPoolExecutor

mainPath = "datasets/gun_classification"

weapClass = ["automaticRifle", "rocketLauncher", "grenadeLauncher", "handgun", "knife", "shotgun", "smg", "sniper", "sword"]

for classes in weapClass:
    os.makedirs(f"{mainPath}/{classes}", exist_ok=True)

def toTrain(weapClass):
    imgPath = "train/images"
    txtPath = "train/labels"

    prefix = f"{weapClass[:3]}*"
    filesImg = glob.glob(os.path.join(mainPath, imgPath, prefix))
    filesTxt = glob.glob(os.path.join(mainPath, txtPath, prefix))

    os.makedirs(os.path.join(mainPath, weapClass, imgPath), exist_ok=True)
    os.makedirs(os.path.join(mainPath, weapClass, txtPath), exist_ok=True)

    for idx, f in enumerate(filesImg):
        ext = os.path.splitext(f)[1]  
        newname = f"{weapClass}_{idx}{ext}"
        shutil.copy(f, os.path.join(mainPath, weapClass, imgPath, newname))
        print(f"[DONE] train: Copied IMG: {newname}")

    for idx, f in enumerate(filesTxt):
        newname = f"{weapClass}_{idx}.txt"
        shutil.copy(f, os.path.join(mainPath, weapClass, txtPath, newname))
        print(f"[DONE] train: Copied TXT: {newname}")
    
def toVal(weapClass):
    imgPath = "val/images"
    txtPath = "val/labels"

    prefix = f"{weapClass[:3]}*"
    filesImg = glob.glob(os.path.join(mainPath, imgPath, prefix))
    filesTxt = glob.glob(os.path.join(mainPath, txtPath, prefix))

    os.makedirs(os.path.join(mainPath, weapClass, imgPath), exist_ok=True)
    os.makedirs(os.path.join(mainPath, weapClass, txtPath), exist_ok=True)

    for idx, f in enumerate(filesImg):
        ext = os.path.splitext(f)[1]  
        newname = f"{weapClass}_{idx}{ext}"
        shutil.copy(f, os.path.join(mainPath, weapClass, imgPath, newname))
        print(f"[DONE] val: Copied IMG: {newname}")

    for idx, f in enumerate(filesTxt):
        newname = f"{weapClass}_{idx}.txt"
        shutil.copy(f, os.path.join(mainPath, weapClass, txtPath, newname))
        print(f"[DONE] val: Copied TXT: {newname}")

def runCopyTrain():
    for classes in weapClass:
        toTrain(classes)
        
def runCopyVal():
    for classes in weapClass:
        toVal(classes)

with ThreadPoolExecutor(max_workers=2) as exe:
    exe.submit(runCopyTrain)
    exe.submit(runCopyVal)