# In this lession we see Type Error , Type Checking , Type Conversion .

# Type Error 
# print(len(123)) # - TypeError int datatype has no len() function.
num_char = len(input("What is your name? "))
# print("Your name has" + num_char + "Characters.")  # - TypeError str can not be concatenate with int.


# type Casting or Conversion 
print("Your name has " + str(num_char) + " Character.")


# Type Checking 
print( type(num_char)) # int data type
print( type("Python")) # str data type
print(type(123.56))    # float data type
bool_var = True
print( type(bool_var)) # beel data type

print( 70 + 100.5) # int + float
print(70 + True)  # True store 1 , False store 0
print( 70 + False) 
