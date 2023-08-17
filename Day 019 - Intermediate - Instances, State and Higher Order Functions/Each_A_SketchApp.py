from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.pensize(10)
tim.pencolor("blue")
tim.shape("arrow")

def move_forwards():
    tim.forward(10)
    tim.pencolor("red")
def move_backwards():
    tim.backward(10)
    tim.pencolor("green")
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.listen()
# Event listener
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()