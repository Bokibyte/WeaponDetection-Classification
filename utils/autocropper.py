import os
import cv2
from ultralytics import YOLO

class autoCropper:
    def __init__(self, modelPath):
        self.model_path = f"runs/{modelPath}/train/weights/best.pt"
        self.model = YOLO(self.model_path)
        self.source_folder = f"datasets/{modelPath}/val/images"
        self.save_folder = f"crops/{modelPath}"
        os.makedirs(self.save_folder, exist_ok=True)
        self.run()

    def run(self):
        image_files = [
            f for f in os.listdir(self.source_folder)
            if f.lower().endswith((".jpg", ".jpeg", ".png"))
        ]
        counter = 0

        for img_name in image_files:
            img_path = os.path.join(self.source_folder, img_name)
            img = cv2.imread(img_path)

            if img is None:
                print(f"Failed to load {img_path}")
                continue

            results = self.model(img, verbose=False)[0]

            for box in results.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                crop = img[y1:y2, x1:x2]

                save_path = os.path.join(self.save_folder, f"{img_name}_crop_{counter}.jpg")
                cv2.imwrite(save_path, crop)
                counter += 1

                print(f"Saved: {save_path}")

        print("\nDone cropping.")
        print(f"Total cropped images: {counter}")
