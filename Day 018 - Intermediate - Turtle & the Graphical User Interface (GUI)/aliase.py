# Importing Modules, Installing Packages, and working with aliases

# Basic import 
import turtle
tim = turtle.Turtle()

# from import

from turtle import Turtle , Screen
#   Module name     things in module

tim = Turtle()
tom = Turtle()
terry = Turtle()


from turtle import * 
# importing everything in turtle module 
forward(100)
from random import *
choice(1,2,3,4)

# Aliases 
import turtle as t
tim = t.Turtle()

# Installing Modules 

import heroes as h
hero = h.gen()
print(hero)