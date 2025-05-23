import csv
import json

# with open("notes.txt", "w") as file:
#     file.write("Continue Learning Python\n")
#     file.write("learn file handling, they are super useful\n")


# with open("notes.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("users.csv","w",newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["name","age","city"])
#     writer.writerow(["phil",30,"Mombasa"])

# #using dict
# with open("users.csv","w",newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=["name","age","city"])
#     writer.writerow({"name":"phil","age":30,"city":"Mombasa"})

# with open("users.csv","r",newline="") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)



#Json

data = {
    "name": "Philip",
    "age": 25,
    "skills": ["python","js"]
}
with open("data.json","w") as file:
    json.dump(data,file, indent=4)

with open("data.json","r") as file:
    content = json.load(file)
    print(f"JSON Data: {content}")

#Json is used in APIS,configuration files