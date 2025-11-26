import os
import shutil
import glob
import yaml

mainPath = "datasets/gun_classification"
rawPath = "datasets/gun_classification/_unstructured"
weapClass = ["automatic_rifle", "bazooka", "grenade_launcher", "handgun", "knife", "shotgun", "smg", "sniper", "sword"]  

def createClassFolder(cls):
    os.makedirs(f"{mainPath}/{cls}", exist_ok=True)
    os.makedirs(f"{mainPath}/{cls}/images/train", exist_ok=True)
    os.makedirs(f"{mainPath}/{cls}/images/val", exist_ok=True)
    os.makedirs(f"{mainPath}/{cls}/labels/train", exist_ok=True)
    os.makedirs(f"{mainPath}/{cls}/labels/val", exist_ok=True)

def copyFile(cls, type):
    prefix = f"{cls[:3]}*"
    getImg = glob.glob(os.path.join(rawPath, type, "images", prefix))
    getTxt = glob.glob(os.path.join(rawPath, type, "labels", prefix))

    for idx, images in enumerate(getImg):
        getImgName = os.path.splitext(os.path.basename(images))[0]
        for labels in  getTxt:
            getTxtName = os.path.splitext(os.path.basename(labels))[0]
            if getImgName == getTxtName:
                newImgName = f"{cls}_{idx}.jpg"
                newTxtName = f"{cls}_{idx}.txt"
                shutil.copy(images, f"{mainPath}/{cls}/images/{type}/{newImgName}")
                shutil.copy(labels, f"{mainPath}/{cls}/labels/{type}/{newTxtName}")
                print(f"[DONE] train img copied : {mainPath}/{cls}/images/{type}/{newImgName}")
                print(f"[DONE] train txt copied : {mainPath}/{cls}/labels/{type}/{newTxtName}")
                break
            
def yamlGen(cls):
    yamlTemplate = {
        "path": f"{mainPath}/{cls}",
        "train": "images/train",
        "val": "images/val",
        "names": {0: cls}
    }
    with open(f"{mainPath}/{cls}/data.yaml", "w") as f:
        yaml.dump(yamlTemplate, f, sort_keys=False)
        
def fixLabels(cls):
    labelsFolder = ["train", "val"]
    
    for folders in labelsFolder:
        labelsFIies = glob.glob(f"{mainPath}/{cls}/labels/{folders}/*.txt")
        
        for file in labelsFIies:
            new_lines = []

            with open(file, "r") as f:
                for line in f:
                    parts = line.strip().split()

                    if len(parts) > 0 and parts[0] != "0":
                        parts[0] = "0"

                    new_lines.append(" ".join(parts))

            with open(file, "w") as f:
                f.write("\n".join(new_lines) + "\n")

            print(f"[UPDATED] Labels with non 0 fixed {file}")
        
for classes in weapClass:
    createClassFolder(classes)
    copyFile(classes, "train")
    copyFile(classes, "val")
    fixLabels(classes)
    yamlGen(classes)
