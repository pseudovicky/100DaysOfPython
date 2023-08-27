# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas

# data = pandas.read.csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
# print(data["temp"])

# data_dict = data_to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# print(data["temp"].mean())
# print(data["temp"].max())

# # get data in columns
# print(data["coondition"])
# print(data.condition)

# # get data in row
# print(data[data.day ==  "Monday"])
# print(data[data.temp == data.temp.max()])


# # Create a dataframe from scratch
# data_dict = {
#     "student": ["Amy", "james", "Vicky"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary fur Color"] == "Grey"])
red_sqirrels_count = len(data[data["primary Fur Color"] == "Cinnamon"])
black_sqirrels_count = len(data[data["primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_sqirrels_count)
print(black_sqirrels_count)

data_dict = {
    "Fur Color" : ["Grey", "Cinnamon", "Black"],
    "Count" : [grey_squirrels_count, red_sqirrels_count, black_sqirrels_count]
}

df = pandas.DataFrame(data.dict)
df.to_csv("squirrel_count.csv")
