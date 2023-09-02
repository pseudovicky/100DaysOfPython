# Different Type of  Errors :-


# 1. FileNotFound Error
with open("a_file.txt") as file:
    file.read()

# Error msg = FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'


# 2. KeyError
a_dictionary = {"key": "value"}
value = a_dictionary["non_existent_key"]

# Error msg = KeyError: 'non_existent_key'



