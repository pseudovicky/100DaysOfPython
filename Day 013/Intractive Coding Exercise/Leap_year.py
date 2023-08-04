year = int(input("Which year do you want to check? "))
# print(type(year))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year")
    else:
        print("leap year")
else:
    print("Not leap year.")

# change input type in int . : 