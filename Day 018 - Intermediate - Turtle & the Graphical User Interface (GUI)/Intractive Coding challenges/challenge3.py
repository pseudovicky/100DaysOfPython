# Draw a triangle, square , pentagon, hexagon, heptagon, octagon, nonagon and decagon.

from turtle import Turtle, Screen
tim = Turtle()
import random
colours = ["red","green","blue","coral","pink","black","SeaGreen","DeepSkyBlue","LightBlue"]
def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)
    
for shape_sides_n in range(3,10):
    tim.color(random.choice(colours))
    draw_shape(shape_sides_n)


screen = Screen()
screen.exitonclick()