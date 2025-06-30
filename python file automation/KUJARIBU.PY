import os
import shutil

# creating folder and files 

new_folder = "laptop file"

if not os.path.exists(new_folder):
    os.mkdir(new_folder)
    print(new_folder)
else:
    print("The folder already exists")


# shutil.rmtree("laptop file")


for items in os.listdir():
    print(items)


# creating and reading in a file 

# with open("example.txt","w") as file:
#     file.write("The fucking kenya power are just disgusting!")



# shutil.copy(f"{new_folder}/example.txt","example.txt")


os.rename("example.txt","kasumbi.txt")
shutil.move("kasumbi.txt",f"{new_folder}/kasumbi.txt")


