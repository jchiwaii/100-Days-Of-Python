print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lowercase = name1.lower()
name2_lowercase = name2.lower()

combined_name = name1_lowercase + name2_lowercase
sum1 = combined_name.count("t") + combined_name.count("r") + combined_name.count("u") + combined_name.count("e") 

sum2 = combined_name.count("l") + combined_name.count("o") + combined_name.count("v") + combined_name.count("e") 

love_score = str(sum1) + str(sum2)

if love_score >= "90" or love_score <= "10":
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= "40" and love_score <= "50":
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

