from turtle import Turtle,Screen
import random
# t = Turtle()
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title='make bet', prompt='Which Turtle will win the race : Enter color:  ')
colors = ['red', 'blue', 'orange', 'yellow', 'purple', 'green']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            if turtle.pencolor() == user_bet:
                print('You Won')
            else:
                print(f'You Lose. {turtle.pencolor()} won')

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
