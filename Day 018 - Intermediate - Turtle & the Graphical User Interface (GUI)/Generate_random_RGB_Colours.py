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

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

directions = [0,90,180,270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))