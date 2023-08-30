from tkinter import *

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Lable(text="I am a lable", font=("Arial", 24, "bold"))
my_label.pack(sidde="left")

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
def button_clicked():
    print("I got clicked")
    my_label.config(text="Button Get Clicked")

button = Button(text="Click Me")
button.pack()

# Entry 
input = Entey(width=10)
input.pack()
print(input.get())


window.mainloop()