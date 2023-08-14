# Method 

class User():

    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001","vicky")
user_2 = User("002","angela")

user_2.follow(user_1)
print(user_2.followers)
print(user_2.following)
print(user_1.followers)
print(user_1.following)