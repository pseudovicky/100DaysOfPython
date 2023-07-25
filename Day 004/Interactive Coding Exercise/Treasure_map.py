#  Treasure Map Exercise

# Don't change the code below
row1 = ["😱","🫣","🫡"]
row2 = ["🥸","🥶","🤩"]
row3 = ["🧐","😝","🥹"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
#  Don't change the code above 

#  Write your code below this line 
# 23
horizontal = int(position[0]) #2
vertical = int(position[1])  #3

selected_row = map[vertical -1 ]
selected_row[horizontal - 1] = "X"

# Don't change the code below
print(f"{row1}\n{row2}\n{row3}")