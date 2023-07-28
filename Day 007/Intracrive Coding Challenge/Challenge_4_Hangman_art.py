
import random 

stages = [
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',   
'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''] 


end_of_game = False
word_list = ["apple","bat","coding","document",'finder','hangman','iphone','mathematics','python','science','machine','github','computer','project']
chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)

# Create a variable called "lives" to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6

# # Testing code
print(f"Pssst, the solution is {chosen_word}.")

#create blanks
display = []
for _ in range(word_lenght):
    display += "_"

# use a while loop to let the user guess again. the loop should only stop once the user 
# has guessed all the letters in the chosen_word and display has no more blanck("_"). 
# then you can tell the user they've won.



while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_lenght):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        

#  if guess is not a letter in the chosen_world,
# then reduce 'lives' by 1.
# if lives goes down to 0 then the game should stop and it should print "you lose".
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose.")


    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You Win")
    
#  print the ASCII art from stages that corresponds to the current number of lives the user has remaining.
    print(stages[lives])