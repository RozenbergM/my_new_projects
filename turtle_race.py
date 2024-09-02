import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which color will win the race?\nChoose the color: "
                                   "(Blue/Orange/Red/Green/Purple/Black)").lower()
is_race_on = False
all_turtles = []

colors = ["blue", "orange", "red", "green", "purple", "black"]
names = ["tim", "tom", "rom", "dom", "som", "angela"]
n = 0
y = -110
for color in colors:
    names[n] = Turtle(shape="turtle")
    names[n].color(color)
    names[n].shapesize(1.5)
    names[n].penup()
    names[n].goto(-220, y)
    all_turtles.append(names[n])
    n += 1
    y += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            if user_bet == turtle.pencolor():
                print(f"You've won! The {turtle.pencolor()} turtle is the winner")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle is the winner")
            is_race_on = False

screen.exitonclick()
