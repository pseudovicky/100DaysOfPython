from turtle import Turtle, Screen

timmy = Turtle()    # Turtle is a class
print(timmy)        # timmy is an object of Turtle class. # printed address of object timmy.
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()