# Different Type of  Errors :-


# 1. FileNotFound Error
with open("a_file.txt") as file:
    file.read()

# Error msg = FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'


# 2. KeyError
a_dictionary = {"key": "value"}
value = a_dictionary["non_existent_key"]

# Error msg = KeyError: 'non_existent_key'


# 3. IndexError 
fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruit_list[3]

# Error msg = IndexError: list index out of range 


# 4. TypeError
name = "Vicky"
age = 23
print(name + age)

# Error msg = TypeError: can only concatenate str (not "int") to str

