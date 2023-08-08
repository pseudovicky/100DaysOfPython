# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# call the greet() function and run your code.

# calling function 
# def greet():
#     print('Hello, World!')
#     print("How are you doing today!")
#     print("Ok, Have a nice day. Good Bye!")

# greet()
# greet()



# input inside function 
# def greet_msg():
#     name = input("What is your name : ")
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
#     print(f"Ok, Have a nice day {name}. Good Bye!")

# greet_msg()


# passing parameter in function
def greet_message(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")
    print(f"Ok, Have a nice day {name}. Good Bye!")

# passing argument in function
username = input("What is your name : ")
greet_message(username)

