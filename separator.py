import os
import glob
import shutil

mainPath = "datasets/gun_classification"
rawPath  = "datasets/gun_classification/_unstructured"

weapClass = [
    "automatic_rifle", "rocket_launcher", "grenade_launcher", 
    "handgun", "knife", "shotgun", "smg", "sniper", "sword"
]

for cls in weapClass:

    imgOutTrain = os.path.join(mainPath, cls, "images", "train")
    imgOutVal   = os.path.join(mainPath, cls, "images", "val")
    lblOutTrain = os.path.join(mainPath, cls, "labels", "train")
    lblOutVal   = os.path.join(mainPath, cls, "labels", "val")

    os.makedirs(imgOutTrain, exist_ok=True)
    os.makedirs(imgOutVal, exist_ok=True)
    os.makedirs(lblOutTrain, exist_ok=True)
    os.makedirs(lblOutVal, exist_ok=True)

    prefix = f"{cls[:3]}*"

    imgTrain = glob.glob(os.path.join(rawPath, "images", "train", prefix))
    imgVal   = glob.glob(os.path.join(rawPath, "images", "val", prefix))
    
    lblTrain = glob.glob(os.path.join(rawPath, "labels", "train", prefix.replace("*","") + "*.txt"))
    lblVal   = glob.glob(os.path.join(rawPath, "labels", "val", prefix.replace("*","") + "*.txt"))

    for idx, img in enumerate(imgTrain):
        name_noext = os.path.splitext(os.path.basename(img))[0]
        ext = os.path.splitext(img)[1]

        newImg = f"{cls}_{idx}{ext}"
        newLbl = f"{cls}_{idx}.txt"

        lbl = os.path.join(rawPath, "labels", "train", name_noext + ".txt")
        if not os.path.exists(lbl):
            print(f"[WARNING] label not found for: {img}")
            continue

        shutil.copy(img, os.path.join(imgOutTrain, newImg))
        shutil.copy(lbl, os.path.join(lblOutTrain, newLbl))

        print(f"[DONE] train copied: {newImg}")

    for idx, img in enumerate(imgVal):
        name_noext = os.path.splitext(os.path.basename(img))[0]
        ext = os.path.splitext(img)[1]

        newImg = f"{cls}_{idx}{ext}"
        newLbl = f"{cls}_{idx}.txt"

        lbl = os.path.join(rawPath, "labels", "val", name_noext + ".txt")
        if not os.path.exists(lbl):
            print(f"[WARNING] label not found for: {img}")
            continue

        shutil.copy(img, os.path.join(imgOutVal, newImg))
        shutil.copy(lbl, os.path.join(lblOutVal, newLbl))

        print(f"[VAL] val copied: {newImg}")
