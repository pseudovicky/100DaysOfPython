'''
Your Life in Weeks

Create a program using maths and f-strings that tells us how many 
days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with 
our time time in this format:
 You have x days, y weeks, and z months that.

Where x,y and z are replaced with actual calculated numbers.

Warning your output should match the Example output  format exactly, even the positions of the commas and full stops.
'''

#  Don't change the code below
age = input("What is your current age?")
# Dont Change the code above

# Write your code below this line

age_as_int = int(age) 
Years_remaining = 90 - age_as_int 
Days_remaining = Years_remaining * 365 
weeks_remaining =  Days_remaining // 7
months_remaining = Years_remaining * 12 

Message = f"You have {Days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left."
print(Message)
