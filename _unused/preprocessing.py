import os
import shutil
import glob
import yaml

class preprocess():
    def __init__(self, inputPath, outputPath, classes):
        
        self.classes = classes
        self.name = inputPath
        self.inputPath = f"datasets/{inputPath}"
        self.outputPath = f"datasets/{outputPath}"
        self.folder = ["train", "val"]
        
        self.prefix = None
        self.yamlPath = None
        self.yamlName = None
        self.yamlExport = None
        
        if not self.classes:
            self.prefix = "*"
        else:
            self.prefix = f"{self.classes[:3]}*"
    
    def createFolder(self):
        [os.makedirs(f"{self.outputPath}/images/{f}", exist_ok=True) for f in self.folder]
        [os.makedirs(f"{self.outputPath}/labels/{f}", exist_ok=True) for f in self.folder]
        
    def copyFile(self):
        self.getImg = sum([glob.glob(f"{self.inputPath}/{f}/images/{self.prefix}") for f in self.folder], [])
        self.getTxt = sum([glob.glob(f"{self.inputPath}/{f}/labels/{self.prefix}") for f in self.folder], [])

        label_map = {os.path.splitext(os.path.basename(t))[0]: t for t in self.getTxt}

        for idx, img in enumerate(self.getImg):
            name = os.path.splitext(os.path.basename(img))[0]
            if name in label_map:
                txt = label_map[name]

                if self.prefix == "*":
                    [shutil.copy(img, f"{self.outputPath}/images/{f}") for f in self.folder]
                    [shutil.copy(txt, f"{self.outputPath}/labels/{f}") for f in self.folder]

                else:
                    newImg = f"{self.classes}_{idx}.jpg"
                    newTxt = f"{self.classes}_{idx}.txt"
                    [shutil.copy(img, f"{self.outputPath}/images/{f}/{newImg}") for f in self.folder]
                    [shutil.copy(txt, f"{self.outputPath}/labels/{f}/{newTxt}") for f in self.folder]

                print(f"[OK] Copied: {name}")
        
    
    def yamlGen(self):

        if self.prefix == "*":
            self.yamlPath = f"{self.outputPath}"
            self.yamlName = self.name
            self.yamlExport = f"{self.outputPath}/data.yaml"
        else:
            self.yamlPath = f"{self.outputPath}/{self.classes}"
            self.yamlName = self.classes
            self.yamlExport = f"{self.outputPath}/{self.classes}/data.yaml"
    
        yamlTemplate = {
            "path": self.yamlPath,
            "train": "images/train",
            "val": "images/val",
            "names": {0: self.yamlName}
        }
        
        with open(self.yamlExport, "w") as f:
            yaml.dump(yamlTemplate, f, sort_keys=False)
            
    def fixLabels(self):
        txt_files = glob.glob(f"{self.outputPath}/{self.classes}/**/*.txt", recursive=True)

        for txt in txt_files:
            with open(txt, "r") as f:
                lines = f.readlines()

            new_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) >= 5:
                    parts[0] = "0"         
                    new_lines.append(" ".join(parts) + "\n")

            with open(txt, "w") as f:
                f.writelines(new_lines)

            print(f"[FIXED] {txt}")

            
