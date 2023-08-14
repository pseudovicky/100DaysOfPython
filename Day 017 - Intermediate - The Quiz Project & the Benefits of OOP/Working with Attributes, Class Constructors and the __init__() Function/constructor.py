# EXAMPLE:-
# # Constructor 

# class Car:
#     """This a car class"""

#     def __init__(self):
#         """This is a __init__ function. initialise attributes. """

class User:

    def __init__(self,user_id,username):
        # print("new user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0

user_1 = User("001","vicky")
print(user_1.username)

user_2 = User("002","angela")
print(user_2.username)

user_3 = User("003","jack")
print(user_3.id)

print(user_1.followers)