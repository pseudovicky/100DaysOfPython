# Create Class 
class User:
    pass
# function inside class
    def userName(fname,lname):
        fullname = fname +  " " + lname
        return fullname

# creating bject
user1 = User()
user2 = User()
print(User.userName("vicky","kumar"))
