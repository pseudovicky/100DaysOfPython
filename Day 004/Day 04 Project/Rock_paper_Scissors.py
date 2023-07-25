# Rock Paper Scissors Game Project Day 4

# Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [ rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock , 1 for Paper and 2 for Scissor.\n"))
print(game_images[user_choice])
import random
computer_choice = random.randint(0,2)
print("Computer choose : ")
print(game_images[computer_choice])

if user_choice >=  3 or user_choice < 0 :
    print("You typed an invalid number, You Lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice :
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")

