from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json
# -------------------------- PASSWORD GENERATOR ----------------------------- #

def generate_password():
    letters = [ "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    symbols = ["!","#","$","%","&","(",")","*","+","_","-"]


    password_letters =  [choice(letters) for _ in range(randint(8,10))]
    password_symboles = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers =  [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symboles + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)



# -------------------------- SAVE PASSWORD ---------------------------------- #

def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = { 
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any feilds empty.")
    else:
        try:
            with open("/Users/vickys-mackbook-air/100DaysOfPython/Day 030 - Intermediate - Errors, Exceptions and JSON Data Improving the Password/Intractive Coding Exercise/data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:        
            with open("/Users/vickys-mackbook-air/100DaysOfPython/Day 030 - Intermediate - Errors, Exceptions and JSON Data Improving the Password/Intractive Coding Exercise/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:    
            # Updating old data with new data
            data.update(new_data)

            with open("/Users/vickys-mackbook-air/100DaysOfPython/Day 030 - Intermediate - Errors, Exceptions and JSON Data Improving the Password/Intractive Coding Exercise/data.json", "w") as data_file:
                # Saving update data
                json.dump(new_data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

#-------------------------find password ----------------------------------#

def find_password():
    website = website_entry.get()
    try:
        with open("/Users/vickys-mackbook-air/100DaysOfPython/Day 030 - Intermediate - Errors, Exceptions and JSON Data Improving the Password/Intractive Coding Exercise/data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exist. ")
            

#------------------- UI SETUP ---------------------------------------- #



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="/Users/vickys-mackbook-air/100DaysOfPython/Day 030 - Intermediate - Errors, Exceptions and JSON Data Improving the Password/Intractive Coding Exercise/logo.png")
canvas.create_image(100 , 100, image=logo_img)
canvas.grid(row=0, column=1)


# Labels

website_label = Label(text="Website:", foreground="#952323")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", foreground="#071952")
email_label.grid(row=2,column=0)
password_label = Label(text="password:", foreground="#0C356A")
password_label.grid(row=3, column=0)

# Entries 
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, )
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "sudovicky@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=13, command= find_password)
search_button.grid(row=1,column=2)
generate_password_button = Button(text="Generate password", command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
