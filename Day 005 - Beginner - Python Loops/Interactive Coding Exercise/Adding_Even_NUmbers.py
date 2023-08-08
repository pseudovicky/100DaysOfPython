'''
# Instruction :
You are ging to write a program that calculate the sum of all the even numbers from 1 to 100.
including 1 and 100.
'''
# Write your code below this row
total_sum = 0
for number in range(1, 101):   # range(1,101, 2) - it's a easiest way 
    if number % 2 == 0:
        total_sum += number 
print(f" Sum of all even number between 1 to 101 is = {total_sum} ")

