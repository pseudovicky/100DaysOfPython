
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

# create an empty list called display.
# for each lletter in the chosen_word , add a "_" to "display" .
# so if the chosen_word was "apple", display should be ["_","_","_","_","_"] with 5 "_" representing each letter to guess.

# letter to guess.
display =[]
word_length = len(chosen_word)
for _ in range(word_length):
    display +=  "_"
print(display) 

guess = input("Guess a letter: ").lower()

# loop through each position in the chosen_word;
# if the letter at that position matches 'guess' then reveal that letter in the display at that position.

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)

# print 'display' and you should see the guessed letter in the correct position and every other letter replacing with "_".
