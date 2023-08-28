# INSTRUCTION 

# Take a look inside file.txt and file2.txt. They each contain a bunch of 
# numbers, each number on a new line 

# You are going to create a list called result which contain the numbers that 
# are common in both files. 
# result = []
with open("/Users/vickys-mackbook-air/100DaysOfPython/Day 026 - Intermediate - List Comprehension and the NATO Alphabet/Intractive Coding Exercise/Challenge 3/file1.txt") as file1:
    file1_data = file1.readlines()

with open("/Users/vickys-mackbook-air/100DaysOfPython/Day 026 - Intermediate - List Comprehension and the NATO Alphabet/Intractive Coding Exercise/Challenge 3/file2.txt") as file2:
    file2_data = file2.readlines()

result = [int(num) for num in file1_data if num in file2_data]

    
print(result)
