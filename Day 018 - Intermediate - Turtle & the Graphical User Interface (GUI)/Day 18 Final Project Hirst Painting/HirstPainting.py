import turtle as turtle_module
from turtle import Screen
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(123, 12, 25), (133, 124, 55),(23,152,45),(113,11,125),(213,211,255),(223,32,65),(193,82,75),(153,162,255),(39,142,125),(179,42,55),(111,152,125),(163,12,25),(123,122,245),(193,79,165),(123,12,25),(193,192,95),(133,102,20)]

tim.setheading(255)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
