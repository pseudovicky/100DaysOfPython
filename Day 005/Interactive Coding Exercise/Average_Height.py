# Instructions 
'''
You are going to write  a program that calculate the average student height from a list of heights.
eg: students_height = [189, 124, 173, 189, 169, 146]
The average height can be calculated by the total number of heights.
eg: 180 + 124 + 165 + 173 + 189 + 169 + 146 + = 1146 
there are a total of 7 height in students_heights 
1146 / 7 = 163.71
average height rounded to the nearest whole number = 164

'''


# Don't Change the code below 
students_heights = input("Input a list of students heights :").split()

for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)
# Don't change tje code above

# write your code below this line

total_height = 0
for height in students_heights:
    total_height += height 
print(total_height) 

number_of_students = 0 
for student in students_heights:
    number_of_students += 1
print(number_of_students)

# total_height = sum(students_heights)
# number_of_students = len(students_heights)
# average_height = round(total_height / number_of_students)
# print(average_height)

