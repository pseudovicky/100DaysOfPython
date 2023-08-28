# INSTRUCTION 

#  You are going to use Dictionary Comprehension to create a dictionary called result that takes 
#  each word in the given sentence and calculates the number of letters in each word.

sentence = "what is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above
result =  { word:len(word) for word in sentence.split() }
# Write your code below:

print(result)