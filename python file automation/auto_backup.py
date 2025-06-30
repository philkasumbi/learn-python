import os
import shutil

source_dir = "code"
backup_dir = "code_backup"


if not os.path.exists(backup_dir):
    os.mkdir(backup_dir)
    print(f"Created folder: {backup_dir}")
 
else:
    print("Folder already exists!")


# backup all .txt files

for file in os.listdir(source_dir):
    if file.endswith(".txt"):
        full_path = os.path.join(source_dir,file)
        shutil.copy(full_path,backup_dir)
        print(f"Backed up: {file}")
