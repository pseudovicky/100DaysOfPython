#  Random Module 
# import module 
import random 

# generate random integer between x and y where x and y is a number
random_integer = random.randint(1, 10)
print(random_integer) 

import My_module
print(My_module.pi)

# generate float number randomly
random_float = random.random() * 5 # default 0.0000000 to 0.9999999...
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

