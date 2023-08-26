# TODO: Create a letter using starting_letter.docs
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend."

# Hint1: This method will help you:
# https://www.w3schools.com/python/ref_file_readline.asp
    # Hint2: This method will also help you:
    # https://www.w3schools.com/python/ref_string_replace.asp
        # Hint3: This method will help you:
        # https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"


with open("/Users/vickys-mackbook-air/100DaysOfPython/Day 024 - Intermediate - Files, Directories and Paths/Mail Merge/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    
with open("/Users/vickys-mackbook-air/100DaysOfPython/Day 024 - Intermediate - Files, Directories and Paths/Mail Merge/Input/Letters/starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"/Users/vickys-mackbook-air/100DaysOfPython/Day 024 - Intermediate - Files, Directories and Paths/Mail Merge/Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)
