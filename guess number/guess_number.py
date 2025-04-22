#create a python program that helps the user to guess numbers

import random

random_number = random.randint(1,10)
counts = 0
guess_limit = 5



while True:
    try:
        user_guess = int(input("Guess a Number: "))
        counts += 1
       

        if user_guess == random_number:
            print(f"Correct you got it in {counts} rounds: ")
            counts = 0
        elif user_guess > random_number:
            print("Too high!")
        else:
            print("Too low!")


        if counts == guess_limit:
            choice = input("You are out of guesses! Do you want to continue (yes/no)?").strip().lower()
            if choice == "yes":
                counts = 0
                random_number = random.randint(1,10)
                print("You have 5 More Guesses")
            else:
                print("Thankyou for playing!")
                break
    except ValueError:
       print("enter a valid number:")