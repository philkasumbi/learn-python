""""
an error is somehting unexpected on your program and python doesnt know how to handle it 
types of errors 
syntax- example print("Hello world" - the opening parenthesis was never closed 
runtime- example zero division error (x = 5 / 0) 

so we use try except 

"""

try:
    #code that might run if there is an KeyError
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"result is: {result}")
except ZeroDivisionError:
     print("You can't divide by zero!")
except ValueError:
     print("Please Enter a valid number")
except:
    #code that runs if there is an error
     print("Oops!, something went wrong")


#debugging
def divide(a,b):
     print(f"Dividing {a} by {b}")
     return a / b
divide(4,5)

#tracebacks
#PEP8 Guidelines

