print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
cross_road = input("You are alone walking in a forest. You find two cross-roads. Which way would you take? Left or Right?\n")
if cross_road == "Left":
   river = input("You take the left route and it leads you to a river. You cannot go back, it is getting dark. You have to make a decision. Do you choose to swim or wait?\n")
else:
    print("The right pathway led you to a pack of wolves. Its game over for you!")
if river == "Swim":
    treasure = input("You struggle and cross the river. You are getting near, you can feel it. You now see three doors that lead to the treasure, a blue, black and red one. Which one would you take?\n")
else:
    print("You wait for some time and it gets dark. After sometime, you see a crowd of lions approaching. Its game over!")
if treasure == "Blue":
    print("Congratulations, you found the treasure.")
elif treasure == "Black":
    print("You opened the black door and you got eaten by a beast")
elif treasure == "Red":
    print("You got burnt by fire")
