weather_c = {
    "mondya":12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thrusday": 14,
    "Friday" : 21,
    "Saturdat": 22,
    "Sunday": 24,
}
# Don't change the code above

# INSTRUCTION 
# You are going to use Dictionary Comprehension to create a dictionary called weather_f
#  that takes each tempreture in degree celcius and convert into degree farenheight.

# To convert temp_c into temp_f : (temp_c * 9/5) + 32 = temp_f 

weather_f = { day:(temp_c*9/5 + 32) for (day, temp_c) in weather_c.items()}

print(weather_f)
