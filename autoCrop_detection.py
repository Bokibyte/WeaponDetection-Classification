import cv2
import os
from ultralytics import YOLO

def main():
    model = YOLO("runs/detect/train/weights/best.pt")  # path model kamu

    source_folder = "datasets/gun_detection/images/val"  # folder yang mau kamu crop
    save_folder = "crops/weapon"
    os.makedirs(save_folder, exist_ok=True)

    image_files = [f for f in os.listdir(source_folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    counter = 0

    for img_name in image_files:
        img_path = os.path.join(source_folder, img_name)
        img = cv2.imread(img_path)

        results = model(img, verbose=False)[0]

        # Loop setiap bounding box
        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            crop = img[y1:y2, x1:x2]

            save_path = os.path.join(save_folder, f"{img_name}_crop_{counter}.jpg")
            cv2.imwrite(save_path, crop)
            counter += 1

            print(f"Saved: {save_path}")

    print("\nDone cropping.")
    print(f"Total cropped images: {counter}")

if __name__ == "__main__":
    main()
