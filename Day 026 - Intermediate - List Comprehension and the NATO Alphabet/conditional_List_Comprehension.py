# new_list = [new_list for item in list if test ]

names = [ "Vicky" , "angela" , "Beth" , "Dave" , "Elanor", "mao" , "jaldi waha se hato" ]
print(names)

short_names = [name for name in names if len(name) < 5 ]

print(short_names)


#  challenge
# Create a new list that contains the names longer than 5 characters in All CAPS.

long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)

