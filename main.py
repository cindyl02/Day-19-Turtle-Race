from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["purple", "blue", "green", "yellow", "orange", "red"]
all_turtles = []
is_race_on = False


def create_turtles():
    starting_y = -100
    for index, color in enumerate(colors):
        tim = Turtle("turtle")
        tim.penup()
        tim.color(color)
        tim.goto(x=-230, y=index * 50 + starting_y)
        all_turtles.append(tim)


def check_answer(color, answer):
    if answer in color:
        print("You win")
    else:
        print(f"You lose. The {color} turtle is the winner.")


def start_race(user_guess):
    global is_race_on
    if user_guess:
        is_race_on = True
    while is_race_on:
        for turtle in all_turtles:
            forward_steps = random.randint(1, 20)
            turtle.fd(forward_steps)
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                check_answer(winning_color, user_guess)
                return


def get_guess():
    return screen.textinput("Make your bet", "Who will win the race? Enter a colour: ")


create_turtles()
guess = get_guess()
start_race(guess)
screen.exitonclick()
