#  Write a program that workd out whether if a given year is a leap year. A mormal year has 365, with an extra day in february.
# The reason why we have leap years is really fascinating, this video it more justice: 

'''
On every year that is evenly divisible by 4 
except every year that is evenly divisible by 100
unless the year is also evenly divisible by 400
'''

#  Don't change the code below 
Year = int(input("which year do you want to check? "))
# Don't change the code above

# Write your code below this line
if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
          print("{Year} is a leap year.")
        else:
            print("{Year} is not a leap year.") 
    else:
        print("{Year} is a Leap year.")
else:
    print("{Year} is not a leap year.")
    