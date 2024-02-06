import random
from logo import art

import random

def check_guess(guess, answer, turns):
    """Check guess against answer and return remaining turns."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return turns

def set_difficulty():
    """Set game difficulty and return corresponding turns."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    elif level == "hard":
        return 5

def game():
    """Main game function."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    turns = set_difficulty()
    print(art)

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_guess(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()
