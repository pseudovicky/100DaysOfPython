# FizzBuzz Job Interview Question 

#  Instructions 
# You are going to write that automatically prints the solution to the FizzBuzz game. 
# your program should print each number from 1 to 100 in turn.
# when the number is divisible by 3 then instead of printing the number it should print "Fizz".
#  When number is divisible by 5, then instead of printing number it should print "Buzz".
#  and if the number is divisible by both 3 and 5 eg. 15 then instead of the number it should print "FizzBuzz".


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0: # Divisible by both 3 and 5 
        print("FizzBuzz")
    elif number % 3 == 0: # Divisible by 3
        print("Fizz")
    elif number % 5 == 0: # Divisible by 5
        print("Buzz")
    else:
        print(number)
        
