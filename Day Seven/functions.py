def greet ():
    print("How are you")
    print("How have you been")
    print("Come back")

greet()

def user (name):
    print(f"Hello {name}")

user("John")


def new (name = input("What is your name?")):
    print(f"My name is {name}")
    
new()

# Keyword Arguments

def greet_now (name = input("your name"), location = input("where_are_you")):
    print(f"Hello {name}")
    print(f"How is {location}")

greet_now()
