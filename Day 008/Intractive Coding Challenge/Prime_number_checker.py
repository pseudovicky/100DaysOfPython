# Instructions
'''
primt number are the number that can only clearly divided by itself and 1.

You need to write a function that checks whether if the number passed into it is a prime number or not.
'''

# Write your code below this line

def prime_checker(number):
    is_prime = True
    for i in range(2, number-1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number.")
        
# Do not change any of the code below
n = int(input("Ckeck this number: "))
prime_checker(number = n)