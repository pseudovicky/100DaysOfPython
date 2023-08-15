# Tuple data type 
# (1,2,3)
# typle is immutable data type 

# my_tuple = (1,3,8)
# print(my_tuple[2]) # indexing

# my_tuple[2] = 12 
# typeError coz its immutable  we cant change it like list.

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

directions = [0,90,180,270]
tim.pensize(15)
tim.speed("fastest")

for _ 