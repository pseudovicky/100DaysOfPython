'''
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output shoult be 3 + 5 = 8.

'''

# Don't Change the code below 
two_digit_number = input("Type a two digit number: ")
# Don't Change the code above 

# Write your code below this line

# Check the data type of two_digit_number
print(type(two_digit_number)) # str

# break through the index then typecast and add both numbers together
result = int(two_digit_number[0]) + int(two_digit_number[1])

# result printing
print(result)