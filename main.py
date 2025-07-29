import pandas
import turtle
from PIL import Image
from titles import Titles

# screen & image

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
img = Image.open(image)
width, height = img.size
screen.setup(width, height)
screen.addshape(image)
turtle.shape(image)

# pandas data

data = pandas.read_csv("50_states.csv")

# code

titles = Titles()

game_loop = True

while game_loop is True:

    answer_state = screen.textinput(title="Gues the state", prompt="What's another state's name?")
    answer_state = answer_state.lower()

    result = data[data["state"].str.lower() == answer_state]

    if not result.empty:
        titles.add_title(int(result.x), int(result.y), result.state.values[0])
    elif answer_state == "quit":
        game_loop = False
    else:
        print(f"stát {answer_state} nenalezen.")


turtle.mainloop()
