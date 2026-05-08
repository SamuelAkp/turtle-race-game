import turtle
import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)


user_bet = screen.textinput("Make your bet", "Which turtle is going will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "purple", "blue"]
all_turtles = []

def create_turtle(x, y_coordinate):
    y = y_coordinate
    for i in range(0,6):
        new_turtle = Turtle(shape= "turtle")
        new_turtle.penup()
        new_turtle.color(colors[i])
        new_turtle.goto(x, y)
        y += 60
        all_turtles.append(new_turtle)

create_turtle(-240, -150)

keep_racing = True

while keep_racing:
    for each_turtle in all_turtles:
        each_turtle.forward(random.randint(0, 5))

        if each_turtle.xcor() >= 230:
            winning_turtle_color = each_turtle.fillcolor()
            keep_racing = False

            if user_bet == winning_turtle_color:
                print(f"You won! {winning_turtle_color} turtle won!")
            else:
                print(f"You lose! You said {user_bet} would win, but {winning_turtle_color} turtle won!")




screen.exitonclick()