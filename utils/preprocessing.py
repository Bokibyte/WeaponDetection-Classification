import os
import shutil
import glob
import yaml


class preprocessing:
    def __init__(self):
        self.mainPath = "datasets/gun_classification"
        self.rawPath = "datasets/gun_classification/_unstructured"
        self.weapClass = [
            "automatic_rifle", "bazooka", "grenade_launcher",
            "handgun", "knife", "shotgun", "smg", "sniper", "sword"
        ]

    def createClassFolder(self, cls):
        os.makedirs(f"{self.mainPath}/{cls}", exist_ok=True)
        os.makedirs(f"{self.mainPath}/{cls}/images/train", exist_ok=True)
        os.makedirs(f"{self.mainPath}/{cls}/images/val", exist_ok=True)
        os.makedirs(f"{self.mainPath}/{cls}/labels/train", exist_ok=True)
        os.makedirs(f"{self.mainPath}/{cls}/labels/val", exist_ok=True)

    def copyFile(self, cls, type):
        prefix = f"{cls[:3]}*"
        getImg = glob.glob(os.path.join(self.rawPath, type, "images", prefix))
        getTxt = glob.glob(os.path.join(self.rawPath, type, "labels", prefix))

        for idx, images in enumerate(getImg):
            getImgName = os.path.splitext(os.path.basename(images))[0]
            for labels in getTxt:
                getTxtName = os.path.splitext(os.path.basename(labels))[0]
                if getImgName == getTxtName:
                    newImgName = f"{cls}_{idx}.jpg"
                    newTxtName = f"{cls}_{idx}.txt"
                    shutil.copy(images, f"{self.mainPath}/{cls}/images/{type}/{newImgName}")
                    shutil.copy(labels, f"{self.mainPath}/{cls}/labels/{type}/{newTxtName}")
                    print(f"[DONE] train img copied : {self.mainPath}/{cls}/images/{type}/{newImgName}")
                    print(f"[DONE] train txt copied : {self.mainPath}/{cls}/labels/{type}/{newTxtName}")
                    break

    def yamlGen(self, cls):
        yamlTemplate = {
            "path": f"{self.mainPath}/{cls}",
            "train": "images/train",
            "val": "images/val",
            "names": {0: cls}
        }
        with open(f"{self.mainPath}/{cls}/data.yaml", "w") as f:
            yaml.dump(yamlTemplate, f, sort_keys=False)

    def fixLabels(self, cls):
        labelsFolder = ["train", "val"]

        for folders in labelsFolder:
            labelsFiles = glob.glob(f"{self.mainPath}/{cls}/labels/{folders}/*.txt")

            for file in labelsFiles:
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

    def processAll(self):
        for cls in self.weapClass:
            self.createClassFolder(cls)
            self.copyFile(cls, "train")
            self.copyFile(cls, "val")
            self.fixLabels(cls)
            self.yamlGen(cls)
