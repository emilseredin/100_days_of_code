import turtle
import random
import colorgram


def get_image_colors(image, num, rgb=True):
    """
        Get <num> colors from an <image> (path)
        Return type: list
        If rgb is set to False, the list will contain Color objects
        Otherwise, it will contain (r, g, b) tuples, where r, g, b are integers
    """
    colors = colorgram.extract(image, num)
    if rgb:
        colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
    return colors


def draw(colors):
    """
        Draw an image, which consists of 10 x 10 circles
        Each circle has a radius of 20px and is filled with a random color taken from an image
        Distance between circles is 50px 
    """
    timmy = turtle.Turtle()
    timmy.speed(20)
    timmy.penup()
    init_x = -410
    init_y = -425
    timmy.sety(init_y)
    for _ in range(10):
        timmy.setx(init_x)
        for _ in range(10):
            color = random.choice(colors)
            timmy.color(color)
            timmy.begin_fill()
            timmy.circle(20)
            timmy.end_fill()
            new_x = timmy.position()[0] + 90
            timmy.setx(new_x)
        new_y = timmy.position()[1] + 90
        timmy.sety(new_y)


def main():
    turtle.setup(width=900, height=900, startx=None, starty=None)
    screen = turtle.Screen()
    screen.colormode(255)
    colors = get_image_colors("/home/emil/Pictures/hirst.jpg", 35)
    draw(colors)
    screen.exitonclick()


if __name__ == "__main__":
    main()
