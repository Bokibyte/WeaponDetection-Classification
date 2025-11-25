import os
import shutil
import glob
from concurrent.futures import ThreadPoolExecutor

mainPath = "datasets/gun_classification"
rawPath = "datasets/gun_classification/_unstructured"

weapClass = ["automatic_rifle", "rocket_launcher", "grenade_launcher", "handgun", "knife", "shotgun", "smg", "sniper", "sword"]  

for classes in weapClass:
    
    os.makedirs(f"{mainPath}/{classes}", exist_ok=True)
    os.makedirs(f"{mainPath}/{classes}/images/train", exist_ok=True)
    os.makedirs(f"{mainPath}/{classes}/images/val", exist_ok=True)
    os.makedirs(f"{mainPath}/{classes}/labels/train", exist_ok=True)
    os.makedirs(f"{mainPath}/{classes}/labels/val", exist_ok=True)

    prefix = f"{classes[:3]}*"
    getImgTrn = glob.glob(os.path.join(rawPath,"train", "images", prefix))
    getTxtTrn = glob.glob(os.path.join(rawPath,"train", "labels", prefix))
    getImgVal = glob.glob(os.path.join(rawPath,"val", "images", prefix))
    getTxtVal = glob.glob(os.path.join(rawPath,"val", "labels", prefix))

    for idx, images in enumerate(getImgTrn):
        getImgName = os.path.splitext(os.path.basename(images))[0]
        for labels in  getTxtTrn:
            getTxtName = os.path.splitext(os.path.basename(labels))[0]
            if getImgName == getTxtName:
                newImgName = f"{classes}_{idx}.jpg"
                newTxtName = f"{classes}_{idx}.txt"
                shutil.copy(images, f"{mainPath}/{classes}/images/train/{newImgName}")
                shutil.copy(images, f"{mainPath}/{classes}/labels/train/{newImgName}")
                print(f"[DONE] train img copied : {mainPath}/{classes}/images/train/{newImgName}")
                print(f"[DONE] train txt copied : {mainPath}/{classes}/labels/train/{newImgName}")
                break
        
    for idx, images in enumerate(getImgVal):
            getImgName = os.path.splitext(os.path.basename(images))[0]
            for labels in  getTxtVal:
                getTxtName = os.path.splitext(os.path.basename(labels))[0]
                if getImgName == getTxtName:
                    newImgName = f"{classes}_{idx}.jpg"
                    newTxtName = f"{classes}_{idx}.txt"
                    shutil.copy(images, f"{mainPath}/{classes}/images/val/{newImgName}")
                    shutil.copy(images, f"{mainPath}/{classes}/labels/val/{newImgName}")
                    print(f"[DONE] val img copied : {mainPath}/{classes}/images/val/{newImgName}")
                    print(f"[DONE] val txt copied : {mainPath}/{classes}/labels/val/{newImgName}")
                    break
                
 