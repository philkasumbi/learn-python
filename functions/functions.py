#a function is a named block of code that performs specific task
# Think of it as a blender and you want to prepare a smoothie 
#you pass variable as parameters
#an argument is the actual value that you pass when calling a  function

def greet(name): #function definition
    print(f"Hello {name}!")
name = input("Enter your name:")
greet(name) #function call (argument)

#a function can also return something not just printing 


def add(a,b):
    return a + b
result = add(6,8)
print(f"The sum is: {result}")


def multiply(a,b):
    return a * b
print(multiply(23,10))


"""
write a function called square(num) that returns the square of a number 
"""

def square(num):
    return pow(num,2)
print(square(6))

"""
write a function that add up three numbers
"""

def add(a,b,c):
    return a + b + c
print(add(1,2,3))

"""
write a function that checks if a number is even 
"""
number = int(input("Enter any any number: "))
    
def checks_even(number):
    
    
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

checks_even(number)

"""
write a function that takes two strings and prints them combined 
"""
def combine_strings(str1,str2):
    return str1 + str2

str1 = input("Enter Your name: ")
str2 = input("Enter Your proffession: ")

combined = combine_strings(str1,str2)
print(f"My name is {str1} and my proffession is {str2}")


#lambda functions - a quick throw away function with no name 

double = lambda x: x * 2
add = lambda a,b: a + b
square = lambda y: y * y

print(double(2))
print(add(10,20))
print(square(8))