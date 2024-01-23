#Program that prints the number of characters in a user's name.

print(len(input("What is your name?"))) #Asks user for name, then prints length of string

name = input("What is your name?") #Saves name in a variable

print(name) #Prints the variable that is saved

#Program that prints the number of characters in a user's name.
name = input("What is your name?")
length = len(name)
print(length)

#Program that interchanges a and b as inputs
a = input("a:")
b = input("b:")

c = a
a = b
b = c

print("a = " + a)
print("b = " + b)