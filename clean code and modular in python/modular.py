from utils import greet #Importing from utils.py
"""
/modularity/
modular means breaking your programs into smaller and managable parts
you can use file or functions
"""

print("Hello, what's Your name:?")
name = input()
print(f"nice to meet you {name}")

def greet_user():
    name = input("Hello, Enter your name: ")
    print(f"nice to meet you {name}")
greet_user()


def add(a,b):
    return a + b 
def subtract(a,b):
    return a - b 
def main():
    print(add(5,7)) 
    print(subtract(5,7))

main() 

result = greet("philippppp")
print(result)