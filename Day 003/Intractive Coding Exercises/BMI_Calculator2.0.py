'''
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.
  - Under 18.5 they are underweight.
  - Over 18.5 but below 25 they have a normal weight.
  - Over 25 but below 30 they are overweight.
  - Over 30 but below 35 they are obese.
  - Above 35 they are clinically obese.
'''


#  Don't Change the code below
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# Don't change the code above

#  Write your code below this line

BMI = weight / height ** 2 
if BMI < 18.5:
    print("You are Underweight.")
elif BMI >= 18.5 and BMI < 25 :
    print("You have a normal weight.")
elif BMI >= 25 and BMI < 30 :
    print("You are Overweight.")
elif BMI >= 30 and BMI < 35 :
    print("you are Obese.")
else:
    print("you are Clinically obese.")