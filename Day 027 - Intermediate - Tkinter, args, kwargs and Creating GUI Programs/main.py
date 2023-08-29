import tkinter

window  = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)



my_label = tkinter.Lable(text="I Am a Lable",font=("Arial",24,"bold"))
my_label.pack(side="left")



import turtle 
tim = turtle.Turtle()
tim.write("Some Text", font=("Times New Roman", 88))
