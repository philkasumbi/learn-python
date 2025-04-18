"""
here goes the task of the day and how i did it  
ask a user for two numbers
print the sum
print the difference 
check if they are equal 
reassign the value of the sum by 10
print a well formatted answer
"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum = num1 + num2
difference = num1 - num2
sum += 10

print(f"The reassigned sum is: {sum}")
print(f"The difference is: {difference}")
print(num1 == num2)