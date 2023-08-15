#  Draw a Random Walk.

import turtle as t
import random

tim = t.Turtle()
tim.pensize(15)
tim.speed("fastest")
colours = ["CornFlowerBlue","LightPink","LightBlue","red","Green","blue","DeepSkyBlue","grey","coral","SeaGreen"]
directions = [0,90,180,270]
for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
