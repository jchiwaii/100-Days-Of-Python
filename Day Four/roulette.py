import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

rand_choice = len(names)
rand_person = random.randint(0, rand_choice - 1)

pay = names[rand_person]
print(pay + " is going to pay the meal today")

# Using choice ()

rand_choice = random.choice(names)
print(rand_choice + " is going to pay the meal today")
