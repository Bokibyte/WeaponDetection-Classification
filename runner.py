from utils.preprocessing import preprocess as prep
from utils.organizer import Organizer
from utils.trainer import YOLOTrainer


weapClass = ["automatic_rifle", "bazooka", "grenade_launcher", "handgun", "knife", "shotgun", "smg", "sniper", "sword"]
yoloModel = "models/yolov8n.pt"

def runTrain():
    for classes in weapClass:
        YOLOTrainer(yoloModel).train(f"gun_classification/{classes}")
        Organizer(f"classification/{classes}").organize()

def runPrep():
    for classes in weapClass:
        p = prep(f"gun_classification/_unstructured", f"gun_classification", classes)
        p.yamlGen()
        p.fixLabels()
        
if __name__ == "__main__":
    runTrain()