# Catching Exceptions :-

# try:  - Something that might cause an exception
# except: - Do this if there was an exception
# else: - Do this if there were no exception
# finally: - Do this no matter what happens

# FileNotFound 

try:
    file = open('/Users/vickys-mackbook-air/100DaysOfPython/Day 030 - Intermediate - Errors, Exceptions and JSON Data Improving the Password/file.txt')
    a_dictionary = { 
        "name": "Vicky Kumar", 
        "age" : 23,
        "course" : "100DayaOfPython",
        "Current_Day" : 30,
        "city": "no",
    }
    print(a_dictionary["city"])
except FileNotFoundError as filename:
    print(f"There was an error in try block! the {filename} is not exist.")
    file = open("/Users/vickys-mackbook-air/100DaysOfPython/Day 030 - Intermediate - Errors, Exceptions and JSON Data Improving the Password/file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist in given dictionary data set.")
    print(a_dictionary["name"]) 
else:
    # if there is no error in try block else block run.
    content = file.read()
    print(content)
finally:
    # it runs everytime no matter what happens is try except and else block.
    file.close()
    print(f" hey, {a_dictionary["name"]}, Now You are in finnaly block.")
    
    # raise an error using raise keyword
    raise KeyError("This is an error that i made up.")
    # raise FileNotFoundError
    # raise IndentationError

