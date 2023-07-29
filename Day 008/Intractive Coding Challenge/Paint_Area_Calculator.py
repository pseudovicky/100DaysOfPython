# Instruction 
'''
You are painting a wall. The instructions on the paint can says that i can of paint cam cover 5 square of wall. 
Given a random height and width of wall.
calculator how many cans of paint you'll need to buy.

number of cans = (wall height * wall width ) + coverage per can.
e.g. Height = 2, width = 4, coverage = 5
number of cans = (2*4)/5 = 1.6
But coz u can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
'''
#write your code below this line
import math
def paint_calc(height,width,cover):
    area = (height * width)
    number_of_cans = math.ceil(area / cover)
    print(f"You'll need {number_of_cans} cans of paint.")


# write your code above this line 

# Don't change the code below
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h,width=test_w,cover=coverage)