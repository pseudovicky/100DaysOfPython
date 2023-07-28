
import random 
word_list = ["apple","bat","coding","document",'finder','hangman','iphone','mathematics','python','science','machine','github','computer','project']
chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)

# Testing code
print(f"Pssst, the solution is {chosen_word}.")

#create blanks
display = []
for _ in range(word_lenght):
    display += "_"

# use a while loop to let the user guess again. the loop should only stop once the user 
# has guessed all the letters in the chosen_word and display has no more blanck("_"). 
# then you can tell the user they've won.

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_lenght):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win")