#  Nested Conditional Statement

print("Welcome to the rollercoaster ride !")
height = int(input("Enter your height in cm? "))

if height >= 120:
    print("Yes you can ride")
    age = int(input("Now, tell me your age in Year !!"))
    if age <= 12:
        print("You have to pay $5")
    elif age > 12 and age <= 18 :
        print("You have to pay $7")
    else:
        print("You have to pay $12")
else:
    print("Sorry, You Can't Ride. you have to grow taller before you can ride.")

