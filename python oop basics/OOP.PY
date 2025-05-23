"""
OOP is a way to organize your code by creating objects that have both data and behaviour
class - blueprint for creating an objects 
object - an instance of a class
when you define and declare a function inside a class is called a method  

def __init__(self):  is a constructor method that runs when you create a new objects
the self parameter is a reference to the current object 
"""


class Car:
    def __init__(self,brand,model,year): 

        self.brand = brand
        self.model = model
        self.year = year
    
    def drive(self):
        print(f"The {self.year} {self.brand} {self.model} is driving")

    def stop(self):
        print("The car has stopped!")

# the result that i get i get after calling my car class thats my object
# you can have diffrent objects from the same class

my_car = Car("Tesla","Model S", 2023)
your_car = Car("Toyota","Corrolla",2022)

my_car.drive()
my_car.stop()
your_car.drive()
your_car.stop()
