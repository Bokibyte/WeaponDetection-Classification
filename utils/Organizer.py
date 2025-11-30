import os
import glob
import shutil

class Organizer:
    def __init__(self, inputPath, movePath):
        self.makeFolder = ["curve", "train", "val", "result"]
        self.loadPath   = f"runs/{inputPath}/train"
        self.movePath   = f"runs/{movePath}/train"

    def organize(self):
        if not os.path.exists(self.loadPath):
            print(f"[ERR] Folder not found: {self.loadPath}")
            return

        all_files = glob.glob(f"{self.loadPath}/*")

        for folder in self.makeFolder:

            dst = f"{self.loadPath}/{folder}"
            os.makedirs(dst, exist_ok=True)

            matched = []

            if folder == "curve":
                matched = [f for f in all_files if "curve" in os.path.basename(f)]

            elif folder == "result":
                matched = [
                    f for f in all_files
                    if any(key in os.path.basename(f) for key in [
                        "results", "matrix", "confusion"
                    ])
                ]

            elif folder == "train":
                matched = [f for f in all_files if "train_batch" in os.path.basename(f)]

            elif folder == "val":
                matched = [f for f in all_files if "val_batch" in os.path.basename(f)]

            for file in matched:
                try:
                    shutil.move(file, dst)
                    print(f"[MOVE] {file} → {dst}")
                except:
                    pass

        os.makedirs(os.path.dirname(self.movePath), exist_ok=True)
        shutil.move(self.loadPath, self.movePath)

        print(f"[DONE] Organized to: {self.movePath}")

