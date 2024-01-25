print( '''
      ____________________________________________________________________
/ \-----     ---------  -----------     -------------- ------    ----\
\_/__________________________________________________________________/
|~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
|  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
| | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
|  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
|~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
|  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
|~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
|    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
| ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
|  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
|~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
| ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
|  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
| ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
|~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
| ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
|~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
| ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
|~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
|____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
/ \----- ----- ------------  ------- ----- -------  --------  -------\
\_/__________________________________________________________________/
'''     )
# Define a function to display the game's introduction
def introduction():
  print("Welcome to the Choose Your Own Adventure game!")
  print("You find yourself in a dark forest, not sure how you got there.")
  print("Your goal is to find your way out and make it back home safely.")

# Define a function to display the options for the first choice
def choice1():
  print("As you walk deeper into the forest, you come across a fork in the road.")
  print("Do you want to go left or right?")
  choice = input("Enter 'L' for left or 'R' for right: ")
  return choice

# Define a function to handle the logic for the first choice
def choice1_logic(choice):
  if choice.upper() == 'L':
    print("You take the left path and come across a clearing with a small cabin.")
    print("Do you want to approach the cabin or keep walking?")
    choice = input("Enter 'A' for approach or 'W' for walk: ")
    return choice
  elif choice.upper() == 'R':
    print("You take the right path and come across a rickety old bridge.")
    print("Do you want to cross the bridge or turn back?")
    choice = input("Enter 'C' for cross or 'B' for back: ")
    return choice
  else:
    print("Invalid choice. Please enter 'L' for left or 'R' for right.")
    return choice1()

# Define a function to handle the logic for the second choice
def choice2_logic(choice):
  if choice.upper() == 'A':
    print("You approach the cabin and find an old man inside.")
    print("He tells you he can help you find your way out of the forest,")
    print("but you need to answer his riddle first.")
    print("What has keys but can't open locks?")
    answer = input("Enter your answer: ")
    if answer.lower() == 'a keyboard':
      print("Correct! The old man points you in the direction of the exit.")
      print("You make it out of the forest and back home safely.")
    else:
      print("Incorrect. The old man grows angry and chases you out of the cabin.")
      print("You run deeper into the forest and lose your way.")
  elif choice.upper() == 'W':
    print("You keep walking and eventually come across a stream.")
    print("Do you want to follow the stream or try to cross it?")
    choice = input("Enter 'F' for follow or 'C' for cross: ")
    return choice
  elif choice.upper() == 'C':
    print("You try to cross the bridge, but it collapses beneath you.")
    print("You fall into the rushing water below and are swept away.")
  elif choice.upper() == 'B':
    print("You turn back and retrace your steps, eventually finding your way out of the forest.")
    print("You make it back home safely.")
  else:
    print("Invalid choice. Please enter 'A' for approach, 'W' for walk, 'C' for cross, or 'B' for back.")
    return choice1_logic(choice1())

# Define a function to handle the logic for the third choice
def choice3_logic(choice):
  if choice.upper() == 'F':
    print("You follow the stream and eventually come across a waterfall.")
    print("Do you want to climb the waterfall or look for another way around?")
    choice = input("Enter 'C' for climb or 'L' for look: ")
    return choice
  elif choice.upper() == 'C':
    print("You try to cross the stream, but the current is too strong.")
    print("You are swept away and lost in the forest.")
  else:
    print("Invalid choice. Please enter 'F' for follow or 'C' for cross.")
    return choice2_logic(choice1_logic(choice1()))

# Define a function to handle the logic for the fourth choice
def choice4_logic(choice):
  if choice.upper() == 'C':
    print("You climb the waterfall and find a hidden cave behind it.")
    print("Inside, you find a treasure chest full of gold and jewels!")
    print("You take the treasure and make your way out of the forest.")
    print("You are hailed as a hero and live happily ever after.")
  elif choice.upper() == 'L':
    print("You look for another way around and eventually come across a path.")
    print("Following the path, you find yourself back at the fork in the road.")
    print("Do you want to go left or right?")
    choice = choice1()
    return choice1_logic(choice)
  else:
    print("Invalid choice. Please enter 'C' for climb or 'L' for look.")
    return choice3_logic(choice2_logic(choice1_logic(choice1())))

# Call the introduction function to start the game
introduction()

# Call the choice1 function to get the user's first choice
choice = choice1()

# Call the choice1_logic function to handle the logic for the first choice
choice = choice1_logic(choice)

# Call the choice2_logic function to handle the logic for the second choice
choice = choice2_logic(choice)

# Call the choice3_logic function to handle the logic for the third choice
choice = choice3_logic(choice)

# Call the choice4_logic function to handle the logic for the fourth choice
choice4_logic(choice)