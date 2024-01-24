# Write a program that works out whether if a given number is an odd or even number.

#Prompt user for number

number = int(input("Which number do you want to check? "))

#Conditional statement
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")