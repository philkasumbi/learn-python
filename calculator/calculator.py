#simple calculator 
import os


result = ""
while True:

    if result == "":
        num1 = float(input("Enter the first number: "))
    else:
        num1 = result
        print(f"continuing with the result: {num1}")  

    num2 = float(input("Enter the second number: "))

    print("   operations   ")
    print("1:addition")
    print("2:subtraction")
    print("3:multiplication")
    print("4:division")
 

    operation = input("choose an operation: ")

    match operation:
        case "1":
            result = num1+num2
            print(result)
        case "2":
            result = num1-num2
            print(result)
        case "3":
            result = num1*num2
            print(result)
        case "4":
            if num2!=0:
                result = num1/num2
                print(result)
            else:
                print("error:cannot divide by zero")
        case "_":
            print("invalid numbers")

#ask if a user wants to continue
    continue_with_result =input("do you want to continue using the result?(yes/no): ")
    if continue_with_result.lower() != "yes":
        result = ""
        os.system("cls")
        break 

