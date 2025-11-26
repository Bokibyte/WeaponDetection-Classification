import glob
import os

def fix_labels(folder):
    txt_files = glob.glob(os.path.join(folder, "*.txt"))

    for file in txt_files:
        new_lines = []

        with open(file, "r") as f:
            for line in f:
                parts = line.strip().split()

                if len(parts) > 0 and parts[0] != "0":
                    parts[0] = "0"

                new_lines.append(" ".join(parts))

        with open(file, "w") as f:
            f.write("\n".join(new_lines) + "\n")

        print(f"[UPDATED] ", file)
        
fix_labels("datasets/gun_classification/sniper/labels/train")
fix_labels("datasets/gun_classification/sniper/labels/val")

