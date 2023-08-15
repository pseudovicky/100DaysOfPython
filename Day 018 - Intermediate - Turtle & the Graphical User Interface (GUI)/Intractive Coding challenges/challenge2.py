# Draw a Dashed Line 

from turtle import Turtle, Screen
tim = Turtle()
tim.shape("turtle")

# logic 1
# for _ in range(15):
#     tim.color("black")
#     tim.forward(10)
#     tim.color("white")
#     tim.forward(10)

# Logic 2
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()