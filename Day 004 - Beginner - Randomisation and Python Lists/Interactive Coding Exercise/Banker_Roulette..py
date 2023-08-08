#  Who's paying Exercise !! 

import random 
# Don't change the code below
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

#  split string method 
nameAsCSV = input("Give me everybody's names, seperated by a comma.  ")
names = nameAsCSV.split(", ")
# DOn't change the code above

# Write your code below this line 
#  get the total number of item in list:
num_items = len(names)
#  generate random numbers between 0 and the last idex.
random_choice = random.randint(0, num_items-1) 
print(random_choice)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today !")