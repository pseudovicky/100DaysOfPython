
#  Day 12 final project The number guessing Game 

import random
from art import welcome

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining. """
    if guess > answer:
        print("too high.")
        return turns - 1
    elif guess < answer:
        print("too low.")
        return turns - 1
    else:
        print(f"you got it ! The answer was {answer}.")

# Make function to set difficulty .
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':  ")
    if level == "easy":
        global turns
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def game():
    # Choosing a random number between 1 and 100.
    print(welcome)
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    print(f"the correct answer is {answer}")

    turns = set_difficulty()
    

    # report the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attemps remaining to guess the number. ")
        # Let the user guess the number.
        guess = int(input("make a guess: "))

        #  Track the number of turns and reduce by 1 if they got it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of gusses, you lose.")
        elif guess != answer:
            print("Guess again !")
game()




