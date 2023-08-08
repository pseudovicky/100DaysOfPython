# Step 1 of HangMan Game 

# set of words
word_list = ["apple","bat","coding","document",'finder','hangman','iphone','mathematics','python','science','machine','github','computer','project']

# randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
word = random.randint(0, len(word_list))
word = word_list[word]
print(word)



# ask the user  to guess a letter and assign their answer to a variable called huess. male guess lowercase.


# check if the letter the user guessed (guess) is ine of the letters in the chosen_word.

guess = input("Guess a letter : ")
for i in word:
    if i == guess.lower():
        print("right")
    else:
        print("Wrong")