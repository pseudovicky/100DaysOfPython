from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))




screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_up, "Down")



screen.exitonclick()