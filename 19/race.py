import turtle
import random


WINDOW_WIDTH = WINDOW_HEIGHT = 900
FINISH_LINE_X = 390
FINISH_LINE_Y = 450


def create_turtle(color):
    t = turtle.Turtle(shape="turtle", visible=False)
    t.color(color)
    t.penup()
    t.shapesize(3, 3)
    return t


def initialize_position(turtle, x, y):
    turtle["turtle"].setx(x)
    turtle["turtle"].sety(y)


def create_turtles():
    init_x = WINDOW_WIDTH // -2 + 30
    init_y = WINDOW_HEIGHT // -2 + 200
    colors = ["red", "blue", "yellow", "green", "brown", "purple"]
    random.shuffle(colors)
    turtles = []
    for i in range(6):
        turtle = {"id": i + 1, "turtle": create_turtle(color=colors.pop()), "finished": False}
        initialize_position(turtle, x=init_x, y=init_y)
        turtle["turtle"].showturtle()
        turtles.append(turtle)
        init_y += 100
    return turtles
    

def draw_finish_line():
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.setx(FINISH_LINE_X)
    t.sety(FINISH_LINE_Y)
    t.pendown()
    t.setheading(-90)
    t.forward(WINDOW_HEIGHT)


def race(turtles):
    keep_running = True
    arrived = []
    turtles_running = len(turtles)
    while keep_running:
        for turtle in turtles:
            if not turtle["finished"]:
                step = random.randint(15, 30)
                turtle["turtle"].forward(step)
                if turtle["turtle"].position()[0] > FINISH_LINE_X:
                    arrived.append(turtle["id"])
                    turtle["finished"] = True
                    turtles_running -= 1
        if turtles_running == 0:
            keep_running = False
    print("Winner: {}".format(arrived[0]))


turtle.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen = turtle.Screen()
screen.colormode(255)
turtles = create_turtles()
draw_finish_line()
race(turtles)
screen.exitonclick()
