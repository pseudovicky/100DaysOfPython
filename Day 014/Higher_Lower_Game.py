from art import logo,vs
from game_date import data
import random

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["discription"]
    account_country = account["country"]
    return f"{account_name}, a{account_descr}, from {account_country}"

def check_answer(guess, a_foloowers, b_followers):
    """Take the user guess and folowers counts and returns if they got it right."""
    if a_foloowers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# display art 
print(logo) 
score = 0 

# Generate random account from the game data.
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b :
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Against B: {format_data(account_b)}")

# ask user for a guess
guess = input("Who has more followers? Type 'A' or 'B' ").lower()

# check if user is correct
# # get follower count of each account.
a_follower_count = account_a["foloower_count"]
b_follower_count = account_b["foloower_count"]
is_correct = check_answer(guess, a_follower_count, b_follower_count)

# Give user feedback on their guess.
# Score keeping
if is_correct:
    score += 1
    print("You're right! Current score: {score}.")
else:
    print("Dorry, that's wrong.")



# make the game repeatable

# Making account at position B become the next account at position A.

# clear the screen between rounds.