#  IndexError 

states_of_india =[ "Andhra Pradesh", "Arunachal Pradesh " , "Assam", "Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir ","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

# print(states_of_india[50])  # indexError

num_of_states = len(states_of_india)
print(num_of_states -1 )

# dirty_dozen = ["Strawberries", "Spinach","Kale","Nectarines","Apples","Grapes","Peaches",
# "Cherries","Pears","Tomatoes","Celery","Potatoes"]

fruits = ["Strawberries","Nectarines","Apples","Grapes","Peaches", "Cherries","Pears"]
vegetables = ["Spinach","kale","Tomatoes","Celery","Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

# access lists inside list - nested indexing
print(dirty_dozen[0][5])
print(dirty_dozen[1][2])