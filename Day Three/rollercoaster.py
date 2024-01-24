print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# Conditional statement

bill = 0

if height > 120:
    print("You can continue to ride")
    age = int(input("How old are you?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
        
    photo = input("Do you want a photo? Y or N.")
    if photo == "Y":
        bill += 3
    print(f"Total bill is ${bill}")
    
else:
    print("Sorry, not possible")
    
# > = : greater than
# < = : less than
# = = : equal to
# = ! : not equal to