# Docstrings 

def format_name(f_name, l_name):
    """Take  a first name and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name}{formated_l_name}"

print(format_name.__doc__)

f_name = input("Enter your first name:")
l_name = input("Enter your last name: ")
print(format_name(f_name,l_name))

