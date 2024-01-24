print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# Conditional statement

if height > 120:
    print("You can continue to ride")
    age = int(input("How old are you?"))
    if age < 12:
        print("You can pay $5")
    elif age <= 18:
        print("You can pay $7")
    else:
        print("You can pay $12")
else:
    print("Sorry, not possible")
    
# > = : greater than
# < = : less than
# = = : equal to
# = ! : not equal to