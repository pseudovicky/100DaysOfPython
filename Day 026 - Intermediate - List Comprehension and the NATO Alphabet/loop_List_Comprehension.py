# for loop with list
# numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)


# for loop in list comprehension
numbers = [1,2,3]
new_list = [n+1 for n in numbers]
print(new_list)

name = "vicky"
letters_list = [letter for letter in name]
print(letters_list)


#  challenge 
# create a new list form a range, where the list items are double the values in the range 

# solution :-
square_list = [i*2 for i in range(1,5)]
print(square_list)


