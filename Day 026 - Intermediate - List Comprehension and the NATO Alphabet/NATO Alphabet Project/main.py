
import pandas 

data = pandas.read_csv("/Users/vickys-mackbook-air/100DaysOfPython/Day 026 - Intermediate - List Comprehension and the NATO Alphabet/NATO Alphabet Project/nato_alphabet.csv")
print(data.to_dict())

# TODO 1: Create a dictionary in this format:
# {"A": "Apple", "B": "Ball"}
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words form a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)