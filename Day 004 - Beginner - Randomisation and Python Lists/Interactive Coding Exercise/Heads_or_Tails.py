#  Heads or Tails Exercise 
'''
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
Important , the first letter shound be capitalised and spelt exactly like in the example e.g. Heads, not heads.

'''

# Remember to use random module
import random
# Don't change the code below
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

#  Write your code below this line
random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")