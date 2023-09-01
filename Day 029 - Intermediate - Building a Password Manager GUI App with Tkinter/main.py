from tkinter import *



# -------------------------- PASSWORD GENERATOR ----------------------------- #

# -------------------------- SAVE PASSWORD ---------------------------------- #

# -------------------------- UI SETUP ---------------------------------------- #



window = Tk()
window.title("Password Manager")
window.config(padx=28, pady=28)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="/Users/vickys-mackbook-air/100DaysOfPython/Day 029 - Intermediate - Building a Password Manager GUI App with Tkinter/logo.png")
canvas.create_image(100 , 100, image=logo_img)
canvas.pack()


window.mainloop()
