import pandas
import turtle
from PIL import Image
from titles import Titles

# screen & image

RESULT_FILE_NAME = "states_to_learn.csv"

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
guessed_states = []
all_states = [n.lower() for n in data.state.to_list()]

while game_loop is True and len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"Gues the state ({len(guessed_states)}/{len(all_states)})", prompt="What's another state's name?")
    answer_state = answer_state.lower()

    result = answer_state in all_states
    state_data = data[data.state.str.lower() == answer_state]

    if result:
        titles.add_title(state_data.x.item(), state_data.y.item(), state_data.state.item())
        guessed_states.append(state_data.state.item().lower())
    elif answer_state == "exit":
        game_loop = False
    else:
        print(f"stát {answer_state} nenalezen.")

missing_states = []
for state in all_states:
    if state not in guessed_states:
        missing_states.append(state)

new_data = pandas.DataFrame(missing_states)
new_data.to_csv(RESULT_FILE_NAME)
