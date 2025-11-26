import os

def addGitkeep(root="datasets"):
    for current_path, dirs, files in os.walk(root):

        skip_list = ["__pycache__", ".git"]

        if any(skip in current_path.replace("\\", "/").split("/") for skip in skip_list):
            continue

        gitkeep_path = os.path.join(current_path, ".gitkeep")

        if ".gitkeep" in files:
            print(f"[SKIP] Already has .gitkeep: {current_path}")
            continue

        with open(gitkeep_path, "w") as f:
            pass

        print(f"[ADDED] .gitkeep: {current_path}")

addGitkeep("datasets")
