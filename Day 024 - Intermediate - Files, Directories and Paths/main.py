# file = open("/Users/vickys-mackbook-air/100DaysOfPython/Day 024 - Intermediate - Files, Directories and Paths/my_file.txt")
# content = file.read()
# print(content)
# file.close()

with open("/Users/vickys-mackbook-air/100DaysOfPython/Day 024 - Intermediate - Files, Directories and Paths/my_file.txt", mode="a") as file:
    content = file.write("\nNew text.")