import turtle
import pandas 

screen = turtle.Screen()
screen.title("U.S State Game")

image = "C:/Users/shubh/Downloads/Udemy 100 days code/day-25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("C:/Users/shubh/Downloads/Udemy 100 days code/day-25/50_states.csv") #need to replace file location
all_states = data.state.to_list()

guessed = []

while len(guessed) < 50:
    answer = screen.textinput(title=f"{len(guessed)}/50 States Guessed", prompt="What's another state name?")

    if answer is None:
        break

    answer = answer.title() 

    if answer == "Exit":
        break

    if answer in all_states and answer not in guessed:
        guessed.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)

turtle.exitonclick()
