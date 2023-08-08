# all you have to do to write a program that takes input first and last name 
# and return output is full name in title case with.

def name(f_name,l_name):
    full_name = f_name +" " + l_name
    result = full_name.title()
    return f"your full name is {result}"

f_name = input("Enter your first name : ")
l_name = input("Enter your last name" )

print(name(f_name,l_name))