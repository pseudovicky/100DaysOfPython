# Project Treasure Island Day 03

print("Welcome to the Treasure Island\nYour mision is to find the treasure.")
direction = input(''' You're at a cross road. Where do you want to go? Type "left" or "right": ''')
if direction == "left" :
    option = input('''You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ''')
    if option == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you you choose? ")
        if door == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")
