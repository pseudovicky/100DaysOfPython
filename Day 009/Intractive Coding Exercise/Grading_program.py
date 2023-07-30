#  Instructions
'''
You have access to a database of student_scores in the format of a dictionary. 
the keys in students_scores are the names of the students and the value are their exam scores.

Write a program that converts their acores to grades. by the end of your program, 
you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.
the final version of the students_grades dictionary will be checked.

'''

student_scores = {
    "Harry": 81,
    "Ron" : 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# Don't change the code above 

# Todo 1 : Create an empty dictionary called student_scores.
student_grades = {}

# Todo 2 : Write your code below to add the grades.

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80 :
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
#  Don't change the code below 
print(student_grades)