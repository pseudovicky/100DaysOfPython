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
    }
    print(a_dictionary["city"])
except FileNotFoundError:
    print("There was an error in try block!")
    file = open("/Users/vickys-mackbook-air/100DaysOfPython/Day 030 - Intermediate - Errors, Exceptions and JSON Data Improving the Password/file.txt", "w")
    file.write("Something")
except KeyError:
    print("That key does not ")
    print(a_dictionary["name"])

