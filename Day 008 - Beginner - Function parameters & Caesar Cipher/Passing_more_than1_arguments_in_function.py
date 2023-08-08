#  Position vs keyword arguments


# def greet(name,location):
#     print(f"Hello {name} from {location}")
#     print(f"what is it like in {location}")

# username = input("What is your name : ")
# city = input("Where are you from: ")
# greet(username,city)


# positional argument - wrong position
# def greet(name,location):
#     print(f"Hello {name} from {location}")
#     print(f"what is it like in {location}")

# username = input("What is your name : ")
# city = input("Where are you from: ")
# greet(city,username)


# keyword argument 
def greet(name,location):
    print(f"Hello {name} from {location}")
    print(f"what is it like in {location}")

username = input("What is your name : ")
city = input("Where are you from: ")
greet(location = city,name = username)