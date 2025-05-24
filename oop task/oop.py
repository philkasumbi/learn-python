
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.grades = []


    def add_grades(self,grade):  
        self.grades.append(grade)
    
    def average_grade(self):
        if self.grades:
            return sum(self.grades)/len(self.grades)
        return 0


    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Avg Grade: {self.average_grade():.2f}"
# instance of class

student1 = Student("philip", 22)


student1.add_grades(85)
student1.add_grades(90)
student1.add_grades(60)
print(student1)
