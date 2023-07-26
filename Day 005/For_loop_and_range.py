#  for loop and the range() function 

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie") 

#  Range()
for number in range(1, 11):
    print(number)

for number in range(1, 11, 2):
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(f"Sum of total number is  = {total} ")
