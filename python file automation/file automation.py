import os
import shutil

#os is for the interaction of file system in your machine and the shutil is for the advanced file operation like copying and moving files
# getcwd is to get the current working directory and listdir is used to list the folders inside the working directory

# explore file system
print(f"Current working directory {os.getcwd}") 

print("listing files and folders")



# create folders and files 

folder_name = "backup_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Created folder: {folder_name}")
 
else:
    print("Folder already exists!")


# creating and reading in a file 

# with open("sample_file.txt","w") as file:
#     file.write("Hello Python! Automate this")
 
# move file to the backup folder
# shutil.move("sample_file.txt", f"{folder_name}/sample_file.txt")

# copy the file back

# shutil.copy(f"{folder_name}/sample_file.txt", "sample_file_copy.txt")

# rename file

# os.rename("sample_file_copy.txt", "copied_file.txt")

# delete file 
# os.remove("copied_file.txt") 
# delete folder
shutil.rmtree(folder_name)

for item in os.listdir():
    print(f" - {item}")