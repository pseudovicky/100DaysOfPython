import random 
from art import stages,logo
# prints the Hangman logo
print(logo)

end_of_game = False
from words import word_list
chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)
lives = 6
display = []
for _ in range(word_lenght):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You Win")
    print(stages[lives])