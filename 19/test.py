import turtle


def move_forwards():
    tim.forward(5)


def move_backwards():
    tim.back(5)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.reset()


tim = turtle.Turtle()
screen = turtle.Screen()
screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()
