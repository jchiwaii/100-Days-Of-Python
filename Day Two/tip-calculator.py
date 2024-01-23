# Instructions

# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6

# Format the result to 2 decimal places = 33.60

# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

print("Welcome to the tip calculator")

bill = input("What was the total bill?")
tip = input("How much tip would you like to give? 10%, 12%, or 15%?")
people = input("How many people to split the bill?")

each_person  = (float(bill) / int(people))*(int(tip)/100 + 1)
each_person_round = "{:.2f}".format(each_person)

print(f"Each person should pay: ${each_person_round}")
