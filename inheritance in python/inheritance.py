# inheritance -lets you reuse code form the parent class
# parent class/ main class
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound!")
# subclass/child class
class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} meows")



dog = Dog("buddy")

dog.speak()
dog.bark()

cat = Cat("whiskers")
cat.speak()
cat.meow()