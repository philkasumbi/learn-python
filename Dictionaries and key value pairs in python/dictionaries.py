#dictionaries and key value pairs
my_dict ={
    "name":"philip",
    "age": 12,
    "is_student": True
}

person = {
    "name": "pablo",
    "age": 45,
    "job": "Engineer"
}

person1 = dict(name = "jake", age = 34, job="Teacher")

print(person["name"])
print(person.get("job" , "Not specified")) #get helps in avoiding errors of the non existent elements

person["status"] = "married"#add values
person["age"] = 49#update values

#delete a value
person.pop("job")
# del person["status"]

print(person["status"])
print(person["age"])

#looping through dictionaries
#key
for key in my_dict:
    print(key)
#loop through values
for value in my_dict.values():
    print(value)

#for both key and value

for key, value in my_dict.items():
    print(f"{key} -> {value}")

"""
create a dictionary called students with keys: name, grade, courses
then, add a new key graduated with values of false
"""

dictionary = {
    "name": "kasumbi",
    "grade": "A",
    "courses": ["s/w engineering","Data Structures","algorithms"]

}


dictionary["graduated"] = False

for key in dictionary:
    print(key)
for value in dictionary.values():
    print(value)

for key, value in dictionary.items():
    print(f"{key} -> {value}")

for course in dictionary["courses"]:
    print("course",{course})




#project -> build a simple phonebook dictionary and allow users to look up contcats 
