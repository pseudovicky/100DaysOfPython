# Swap Program 

# Don't change the code below 
a = input("a:")
b = input("b:")

# Write Your code below this line !
# a,b = b,a # simple solution.
# type casting string to integer
a = int(a)
b = int(b)

# Swap logic
a = a + b 
b = a - b
a = a - b 

# type casting integer to string
a = str(a)
b = str(b)

# Don't change the code below
print("a = " + a)
print("b = " + b)