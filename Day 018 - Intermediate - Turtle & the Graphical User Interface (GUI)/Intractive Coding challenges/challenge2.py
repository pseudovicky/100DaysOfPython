# Draw a Dashed Line 

from turtle import Turtle, Screen
tim = Turtle()
tim.shape("turtle")
for i in range(15):
    tim.color("black")
    tim.forward(10)
    tim.color("white")
    tim.forward(10)


screen = Screen()
screen.exitonclick()