# hint 4 : create a deal_card() function that uses the list below to return a random card.
# 11 is the Ace.
import random
import os
from art import logo 
def deal_card():
    '''Returns a random card from the deck.'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

# hint 6 : createa function called calculate_score() that takes a list of cards as input and returns the score .
# Look up the sum() function to help you do this.
def calculate_score(cards):
    '''thake a list of cards and return the score calculated from the cards'''
    # hint 7 : Inside calculate_score() check for a blackjack (a hand with 2 cards: ace + 10)
    # and retrun 0 instead of the actual score : 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # hint 8 : Inside calculate_score() check for an 11(ace). if the score is already over 21, 
    # remove the 11 and replace it with 1. you might need to look up append() and remove.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
# hint 13 : Create a function called compare() and pass the user)score and computer_score . if the computer 
#  and user both have the same score. then it's a draw. if the computer has a blackjack (0). then the user loses.
#  then the user loose . if the user has a blackjack(0). then the user wins. if the blackjack
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack "
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score == 21:
        return "You went over. You Lose "
    elif computer_score > 21:
        return "Oppenent went over. You win"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You lose"

def play_game():
    print(logo)
# hint 5 : Deal the user and computer 2 cards each using deal_card()
user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())    

    # hint 11 : The score will need to be rechecked with every new cardd draw and the checks in hint 
    #  9 need to be repeated until the game ends.
# while not is_game_over:

# hint 9 : call calculate_score(). if the computer or the user has a blackjack (0) or 
# if the user's score is over 21, then the game ends.
user_score = calculate_score(user_cards)
computer_score = calculate_score = calculate_score(computer_cards)
print(f" your cards : {user_cards}, current score : {user_score}")
print(f" Computer's first card: {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
else:
    # hint 10 : if the game has not ended, ask the user if they want to draw another card. if yes, then
    # use the dead_card() function to add another card to the user_cards list. if no, then the game has ended.
    use_should_deal = input ("Type 'y' to get another card, type 'n' to pass: ")
    if use_should_deal == "y":
        user_cards.append(deal_card())
    else:
        is_game_over = True


# hint 12 : Once the user is done and no longer wants to draw more cards , it's time to let the  
#  computer play . The computer should keep drawing cards as long as it has a score less than 17.
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
print(f" Your final hand: {user_cards}, final score: {user_score}")
print(f" Computer's final hand: {computer_cards}, fial score : {computer_score}")
print(compare(user_score, computer_score))

# hint 14 : Ask the user if they want to restart the game . 
# if they answer yes, claer the consol and start a new game of blackjack and  show the logo from art.py
while input("Do you want to play a game of blackjack? type 'y' or 'n' : " ) == "y":
    os.clear()
    play_game()
