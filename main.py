import turtle
from PIL import Image

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
img = Image.open(image)
width, height = img.size
screen.setup(width, height)

screen.addshape(image)
turtle.shape(image) 

answer_state = screen.textinput(title="Gues the state", prompt="What's another state's name?")
print(answer_state)


turtle.mainloop()
