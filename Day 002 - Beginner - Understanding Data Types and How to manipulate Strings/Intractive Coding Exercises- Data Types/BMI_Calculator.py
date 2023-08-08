'''
Write a program that calculates the body mass index (BMI) from a user's weight and height.
BMI = weight(kg) / height^2 (m^2)
'''
# Don't change the code below
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# Don't change the code above

# Write your code below
height = float(height)
weight = float(weight) 

BMI = weight / height ** 2
print("bmi as int = " , int(BMI))

