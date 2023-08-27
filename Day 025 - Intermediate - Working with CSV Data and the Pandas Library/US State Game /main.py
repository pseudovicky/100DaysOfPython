import turtle

screen = turtle.Screen()
screen.titlr("U.S. States Game")
image = "blank_states_img.jpg"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
print(answer_state)


