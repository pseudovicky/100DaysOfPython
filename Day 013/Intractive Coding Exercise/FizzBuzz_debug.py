for number in range(1,101):
    print(f"Currently on number {number} ")
    if number %3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print([number])

# there is lot of if on same indentation .
# instead of if another if use elif.
# change or to and.