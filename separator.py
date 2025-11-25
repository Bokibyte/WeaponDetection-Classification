import os
import shutil
import yaml

def ensure(path):
    os.makedirs(path, exist_ok=True)

def get_classname(filename):
    # Ambil nama sebelum underscore pertama
    # Contoh: "Automatic Rifle_10.jpeg" → "Automatic Rifle"
    name = filename.rsplit(".", 1)[0]
    parts = name.split("_")
    return parts[0] if len(parts) > 1 else name

def process_split(split_type):
    """
    split_type = 'train' atau 'val'
    """
    src_images = f"datasets/gun_classification/{split_type}/images"
    src_labels = f"datasets/gun_classification/{split_type}/labels"

    dst_images = f"datasets/gun_classification/structured/{split_type}/images"
    dst_labels = f"datasets/gun_classification/structured/{split_type}/labels"

    ensure(dst_images)
    ensure(dst_labels)

    # buat counter per-class
    counters = {}

    files = [f for f in os.listdir(src_images) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    for img_file in files:
        classname = get_classname(img_file)

        # Increment counter untuk class ini
        if classname not in counters:
            counters[classname] = 1
        else:
            counters[classname] += 1

        # Ekstensi file
        ext = img_file.split(".")[-1]

        # Nama file baru
        new_name = f"{classname}_{counters[classname]}.{ext}"

        # Path sumber
        img_src = os.path.join(src_images, img_file)
        txt_src = os.path.join(src_labels, img_file.rsplit(".", 1)[0] + ".txt")

        # Path tujuan
        img_dst_folder = os.path.join(dst_images, classname)
        txt_dst_folder = os.path.join(dst_labels, classname)

        ensure(img_dst_folder)
        ensure(txt_dst_folder)

        # Copy + rename image
        shutil.copy(img_src, os.path.join(img_dst_folder, new_name))

        # Copy label dengan nama baru
        if os.path.exists(txt_src):
            new_label_name = new_name.rsplit(".", 1)[0] + ".txt"
            shutil.copy(txt_src, os.path.join(txt_dst_folder, new_label_name))

        print(f"Moved: {img_file} → {classname}/{new_name}")

def create_yaml():
    base_path = "datasets/gun_classification/structured"
    train_images = os.path.join(base_path, "train", "images")

    # ambil semua folder class di train/images/
    classes = [d for d in os.listdir(train_images) if os.path.isdir(os.path.join(train_images, d))]

    classes.sort()

    names_dict = {i: cls for i, cls in enumerate(classes)}

    yaml_dict = {
        "path": base_path,
        "train": "train/images",
        "val": "val/images",
        "names": names_dict
    }

    yaml_path = os.path.join(base_path, "data.yaml")

    with open(yaml_path, "w") as f:
        yaml.dump(yaml_dict, f, sort_keys=False)

    print("\n✓ data.yaml dibuat otomatis!")
    print(f"Lokasi: {yaml_path}")
    print("Isi names:", names_dict)

def main():
    process_split("train")
    process_split("val")
    print("\n✓ Dataset berhasil direstrukturisasi!")
    create_yaml()

if __name__ == "__main__":
    main()
