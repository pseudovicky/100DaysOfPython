# ------------------- COSNTANTS----------------------- #

from tkinter import *

PINK = "#e2979c"
RED = "#e7205b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

#------------------------- TIMER RESET --------------------#


#------------------------- TIMER MACHANISM -----------------#


#------------------------- COUNTDOWN MACHENISM --------------#


# ------------------------ UI SETUP --------------------------#

window = Tk()
window.title("Pomodoro")
window.config(padx=40,pady=40, bg= YELLOW)

canvas = Canvas(width=348, height=348, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="/Users/vickys-mackbook-air/100DaysOfPython/Day 028 - Intermediate - Tkinter, Dynamic Typing and the Pomodoro GUI Application/pomodoro.png")
canvas.create_image(174,174, image=tomato_img)
canvas.create_text(174, 174, text="00:00" , fill="white", font=(FONT_NAME, 24, "bold") )
canvas.pack()








window.mainloop()
