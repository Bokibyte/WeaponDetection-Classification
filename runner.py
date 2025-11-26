from utils.preprocessing import preprocess as prep
from utils.trainer import YOLOTrainer
from utils.organizer import Organizer

weapClass = ["automatic_rifle", "bazooka", "grenade_launcher", "handgun", "knife", "shotgun", "smg", "sniper", "sword"]
yoloModel = "models/yolov8n.pt"

def runTrain():
    for classes in weapClass:
        YOLOTrainer(yoloModel).train(f"gun_classification/{classes}")
        Organizer(classes)
        
if __name__ == "__main__":

    for classes in weapClass:
        p = prep(f"gun_classification/_unstructured", f"gun_classification", classes)

        p.yamlGen()
        p.fixLabels()
    
