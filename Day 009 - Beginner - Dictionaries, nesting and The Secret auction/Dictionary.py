# The python Dictioonary Deep Dive 

# Key : Value 
# Bug   : An error in program that prevents the program from running as expected. 

# { Key : Value}

user_data = {"name":"vicky kuamr" , 
            "age":23,
            "country":"India",
            "course":"100DaysOfPython",
            "num":[1,2,3,4,5,6,7]
             }

index0 = user_data["name"]
print(index0) 
print(user_data["num"])

# adding new items 
user_data["language"] = ("English","Hindi")

print(user_data)

# Edit an item 

user_data["num"] = [10,9,8,7,6,5,4,3,2,1]
print(user_data)

# Loop through a dictionary
for key in user_data:
    print(user_data[key])