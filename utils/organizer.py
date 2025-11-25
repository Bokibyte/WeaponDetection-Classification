import os
import glob
import shutil

class Organizer:
    def __init__(self, contextName: str):

        self.folderPath = f"runs/{contextName}/train"
        self.orgFolder = ["curve", "train", "val", "result"]
        self.resultFolder = ["labels", "result", "confusion"]
        self.run()

    def move_files(self, pattern, target):
        files = glob.glob(pattern)
        for file in files:
            shutil.move(file, target)
            print(f"Moved: {file} -> {target}")

    def run(self):
        for nameFolder in self.orgFolder:

            if nameFolder == "curve":
                target = f"{self.folderPath}/{nameFolder}"
                os.makedirs(target, exist_ok=True)

                pattern = f"{self.folderPath}/*curve*"
                self.move_files(pattern, target)

            elif nameFolder == "result":
                target = f"{self.folderPath}/{nameFolder}"
                os.makedirs(target, exist_ok=True)

                for resultName in self.resultFolder:
                    pattern = f"{self.folderPath}/{resultName}*"
                    self.move_files(pattern, target)

            else:
                target = f"{self.folderPath}/{nameFolder}"
                os.makedirs(target, exist_ok=True)

                pattern = f"{self.folderPath}/{nameFolder}*"
                self.move_files(pattern, target)

        print("\n[DONE MOVE]")
