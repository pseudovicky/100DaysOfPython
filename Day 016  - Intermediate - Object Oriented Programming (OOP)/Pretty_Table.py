from prettytable import PrettyTable

table = PrettyTable()
print(table)
# using row
table.field_names = ["pokemon Name","Type"]
table.add_rows([
    ["Pikachu","Electric"],
    ["Squirtle","Water"],
    ["Charmander","Fire"],
])
print(table)


# using column
table2 = PrettyTable()
table2.add_column("Pokemon_name", ["pikachu","squirtle","charmander"])
table2.add_column("Type",["Electric","water","fire"])
print(table2)
print(table2.align) # c means Center 
table2.align = "l"
print(table2)
print(table2.align)

