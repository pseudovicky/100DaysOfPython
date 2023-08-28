student_dict = {
    "student" : ["Vicky", "Angela","James","Lily"],
    "score" : [79,56,76,68]
}

#  Looping through dictionaries: 
for (key, value) in student_dict.items():
    print(key,value)

import pandas 

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a data frame 
for (key,value) in student_data_frame.items():
    print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(index)
    if row.student == "Vicky":
        print(row.score)
        