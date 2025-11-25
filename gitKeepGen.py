import os

def addGitkeep(root="."):
    for current_path, dirs, files in os.walk(root):

        skip_list = ["__pycache__", ".git"]

        if any(skip in current_path.replace("\\", "/").split("/") for skip in skip_list):
            continue

        if len(files) == 0 and len(dirs) == 0:
            gitkeep_path = os.path.join(current_path, ".gitkeep")

            if not os.path.exists(gitkeep_path):
                with open(gitkeep_path, "w") as f:
                    pass
                print(f"[ADDED] .gitkeep: {current_path}")
            else:
                print(f"[SKIP] .gitkeep already exists: {current_path}")

        else:
            print(f"[SKIP] has files or subfolders: {current_path}")

addGitkeep(".")
