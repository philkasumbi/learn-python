class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working!!")

class Manager(Employee):
    def work(self):
        print(f"{self.name} is managing the Team")


class Developer(Employee):
    def work(self):
        print(f"{self.name} is writing code")


manager = Manager("philip",3000)

manager.work()
print(manager)

developer = Developer("kelvin",5000)
developer.work()
print(developer)

