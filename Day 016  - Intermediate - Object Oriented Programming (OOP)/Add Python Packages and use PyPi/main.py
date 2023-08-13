from prettytable import PrettyTable

data = PrettyTable()

data.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
data.add_row(["Adelaide", 1295, 1158259, 600.5])
data.add_row(["Brisbane", 5905, 1857594, 1146.4])
data.add_row(["Darwin", 112, 120900, 1714.7])
data.add_row(["Hobart", 1357, 205556, 619.5])
data.add_row(["Sydney", 2058, 4336374, 1214.8])
data.add_row(["Melbourne", 1566, 3806092, 646.9])
data.add_row(["Perth", 5386, 1554769, 869.4])

# print(data)

data.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)

print(data)
print(type(data))
mystring = data.get_string() 
print(mystring)
print(type(mystring)) 

