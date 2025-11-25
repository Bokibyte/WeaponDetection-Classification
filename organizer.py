import os
import glob
import shutil

contextName = "detection"

folderPath = f"runs/{contextName}/train"
orgFolder = ["curve", "train", "val", "result"]
resultFolder = ["labels", "result", "confusion"]

for nameFolder in orgFolder:

    if nameFolder == "curve":
        target = f"{folderPath}/{nameFolder}"
        os.makedirs(target, exist_ok=True)

        files = glob.glob(f"{folderPath}/*curve*")
        for file in files:
            shutil.move(file, target)
            print(f"Moved: {file} -> {target}")

    elif nameFolder == "result":
        for resultName in resultFolder:
            target = f"{folderPath}/{resultName}"
            os.makedirs(target, exist_ok=True)
            files = glob.glob(f"{folderPath}/{resultName}*")

            for file in files:
                shutil.move(file, target)
                print(f"Moved: {file} -> {target}")

    else:
        target = f"{folderPath}/{nameFolder}"
        os.makedirs(target, exist_ok=True)
        files = glob.glob(f"{folderPath}/{nameFolder}*")
        for file in files:
            shutil.move(file, target)
            print(f"Moved: {file} -> {target}")
            
print("\n[DONE MOVE]")
