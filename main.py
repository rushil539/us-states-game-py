import turtle
import pandas
from states import States

screen = turtle.Screen()
data = pandas.read_csv(r"C:\Workspace\Python\us_states_game\50_states.csv")
screen.title("U.S. STATES GAME")
image = r"C:\Workspace\Python\us_states_game\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = data["state"].to_list()
correct_ans = []
states_found = []

while len(correct_ans) < 50:
    user_ans = screen.textinput(f"{len(correct_ans)}/50 States Correct", "What's another state's name?").title()
    if user_ans in states and user_ans not in correct_ans:
        state = data[data["state"] == user_ans]
        x = int(state.x.iloc[0])
        y = int(state.y.iloc[0])
        states_found = States(x, y, user_ans)
        new_state = user_ans
        correct_ans.append(new_state)

    elif user_ans == "Exit":
        missing_states = [missed_state for missed_state in states if missed_state not in correct_ans]
        data = pandas.DataFrame(missing_states)
        data.to_csv(r"C:\Workspace\Python\us_states_game\missing_states.csv")
        break

    


screen.exitonclick()


