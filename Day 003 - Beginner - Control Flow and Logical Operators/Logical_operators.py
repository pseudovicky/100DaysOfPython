#  and   or   not  operators.

#  RollerCoaster ride Ticket Program.

print("Welcome to the roallerCoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You acn ride the rollerCoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("child tickets are $5.")
        bill += 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill += 7
    elif age >= 45 and age <= 55:  
        print("Everything is going to be ok. have a free ride on us!") # coz of middlelife crisis.

    else:
        print("Adult tickets are $12.")
        bill += 12
        
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" or "y" :
        # Add $3 to their bill
        bill += 3
    
    print(f"Your final Bill is {bill}.")

else:
    print("Sorry, you have to grow taller before you can ride.")