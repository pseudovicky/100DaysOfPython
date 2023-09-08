from tkinter import *
BACKGROUND_COLOR = '#B1DDC6'

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='image/card_font.png')
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text='Title', font=('Arial', 40, 'Italic'))
canvas.create_text(400, 263, text='word', font=('Arial', 68, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightbackground=0)
canvas.grid(row=0, column=0)
cross_image = PhotoImage(file='Image/wrong.png')
unknown_button = Button(image=cross_image)
unknown_button.grid(row=1, column=0)
check_image = PhotoImage(file='images/right.png')
known_button =Button(image=check_image, highlightbackground=0)
known_button.grid(row=1, column=1)




window.mainloop()