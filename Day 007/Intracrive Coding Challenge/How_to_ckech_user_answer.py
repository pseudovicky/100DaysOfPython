# Step 1 of HangMan 1 - start

# set of words
word_list = ["apple","bat","coding","document",'finder','hangman','iphone','mathematics','python','science','machine','github','computer','project']

# randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

chosen_word = random.choice(word_list)



# ask the user  to guess a letter and assign their answer to a variable called huess. make guess lowercase.

guess = input("Guess a letter: ").lower()

# check if the letter the user guessed (guess) is ine of the letters in the chosen_word.

for letter in chosen_word:
    if letter == guess:
        print('Right')
    else:
        print('Wrong')

