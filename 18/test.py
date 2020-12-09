from turtle import Turtle, Screen, mode
import random


def get_random_color():
    r = random.randint(0, 255)
    g = random_r = random.randint(0, 255)
    b = random_r = random.randint(0, 255)
    return r, g, b


def draw_polygon(sides, side_length, turn_direction):
    # the angle between the current direction line and the next direction line
    angle = 360 / sides
    for i in range(sides):
        timmy.forward(side_length)
        if turn_direction == "left":
            timmy.left(angle)
        else:
            timmy.right(angle)


def draw_dashed_line(dash_count, dash_len):
    for i in range(dash_count * 2):
        if i % 2 == 0:
            timmy.pendown()
        else:
            timmy.penup()
        timmy.forward(dash_len)


def draw_shapes():
    for i in range(3, 11):
        timmy.pencolor(get_random_color())
        draw_polygon(sides=i, side_length=100, turn_direction="right")


def random_walk():
    for _ in range(100):
        rand_angle = random.random() * 360
        timmy.setheading(rand_angle)
        timmy.forward(40)


def random_orientation_walk():
    directions = [0, 90, 180, 270]
    for _ in range(200):
        timmy.pencolor(get_random_color())
        h = random.choice(directions)
        timmy.setheading(h)
        timmy.forward(30)


def spirograph():
    heading = 0
    # angle increment for each new circle
    increment = 5
    radius = 200
    timmy.pensize(1)
    timmy.speed(20)
    for _ in range(360 // increment):
        timmy.pencolor(get_random_color())
        timmy.circle(radius)
        heading += increment
        timmy.setheading(heading)


timmy = Turtle()
screen = Screen()
# timmy.shape("turtle")
screen.colormode(255)
# draw_polygon(4, 100)
# draw_dashed_line(15, 10)
# draw_shapes()
# random_walk()
# random_orientation_walk()
spirograph()
screen.exitonclick()
