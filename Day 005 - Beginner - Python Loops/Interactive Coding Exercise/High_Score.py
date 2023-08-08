# HIGH SCORE
# Introductions

# you are going to program that calculates that highest score from a list of scores. 
# eg students scores = [78, 65 , 85, 86, 55, 91, 64, 89 ]
# impotant you are not allowed to use the max or min functions. the output words must match the example.i.e 
# the gigh score in the classs is : x

#  Don't change the code below 
student_scores = input("Input the list of students scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
#  Don't change the code above 

#  Write your code below this row

# print(max(student_scores))
# print(min(student_scores))

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")


