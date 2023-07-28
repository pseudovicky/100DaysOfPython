
# Replacing blanks with guesses

# Step 1 of HangMan 1 - start

# set of words
word_list = ["apple","bat","coding","document",'finder','hangman','iphone','mathematics','python','science','machine','github','computer','project']

# randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

chosen_word = random.choice(word_list)

# Testing code 
print(f"pssst, the solution is {chosen_word}.")


# ask the user  to guess a letter and assign their answer to a variable called huess. make guess lowercase.

guess = input("Guess a letter: ").lower()

# create an empty list called display.
# for each lletter in the chosen_word , add a "_" to "display" .
# so if the chosen_word was "apple", display should be ["_","_","_","_","_"] with 5 "_" representing each letter to guess.


for letter in chosen_word:
    if letter == guess:
        print('Right')
    else:
        print('Wrong')

