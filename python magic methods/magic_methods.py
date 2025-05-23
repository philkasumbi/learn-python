class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof!")

    def __str__(self):
        return f"{self.name} is {self.age} years old"

my_dog = Dog("Buddy",3)
print(my_dog)

# class -> object -> method 
# danda methods 
# __init__,__len__,__str__,__add__,etc - they let you customise how objects behave in certains situations in your code


class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author= author
        self.pages = pages
        
    def __str__(self):
        return f"'{self.title}' by {self.author} - {self.pages} pages"
    
    # create a book instance 
book1 = Book("1984","gorge orwell",328)
print (book1)

        