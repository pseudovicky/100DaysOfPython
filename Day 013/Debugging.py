################DEBUGGING################################

# # Desccribe problem
# def my_function():
#     for i in range(1, 20): 
#         if i == 20:
#             print("You got it")
# my_function()
# # bug report :
# # range is between 1 to 20 that means last value of i is 19 . 


# # Reproduce the Bug 
# from random import randint
# dice_imgs = ["1","2","3","4","5","6"]
# dice_num = randint(0,5)
# print(dice_imgs[dice_num])
# # Bug Report:
# # list index starts from 0 so change the range 1,6 to 0,5.


# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a Gen millenial")
# elif year >= 1994:
#     print("You are a Gen Z.")
# #Bug Report:
# # 1994 input has no output in this program so change the > instead of >= sign.


# # Fix the Errors 
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"you can drive at age {age}.")
# # Bug report:
# # input type is by default strings which is not perform numrical operations.
# # change input type int in line 33.
# # fix indentation in line 35.
# # write f before print msg.


# #print is your friend
# page = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# # print(pages)
# word_per_page = int(input("Number of words per page: "))
# # print(word_per_page)
# total_words = pages * word_per_page 
# print(total_words)
# # Bug report:
# # instead of == write = . i  word_per_page input code.


# Use a debugger 
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)
mutate([1,2,3,4,5,8,13])
# Bug report:
# there is just a undentation problem in line 61 indented it inside the for loop.

# final debugging tips 
# Take a break 
# ask a friend 
# run often - run it after every execution.
# ask StackOverflow


