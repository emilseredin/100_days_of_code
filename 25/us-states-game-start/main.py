from turtle import Turtle, Screen
import csv


def parse_csv():
    states = {}
    with open("50_states.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            state_name = row["state"].lower()
            x = int(row["x"])
            y = int(row["y"])
            states.update({
                state_name: { 
                    "x": x,
                    "y": y
                }
            })
    return states


def play(screen):
    states = parse_csv()
    turtle = Turtle()
    turtle.penup()
    turtle.hideturtle()
    keep_going = True
    guessed_states = 0
    input_title = "Guess the state"
    while keep_going:
        answer = screen.textinput(title=input_title, prompt="Enter the state name (type 'q' to quit): ").lower()
        if answer == "q":
            keep_going = False
        elif answer in states:
            guessed_states += 1
            turtle.setx(states[answer]["x"])
            turtle.sety(states[answer]["y"])
            turtle.write(answer.capitalize())
            input_title = "{}/50 States Correct".format(guessed_states)
        

def main():
    screen = Screen()
    screen.title("U.S.A. States game")
    screen.bgpic("blank_states_img.gif")
    play(screen)
    screen.exitonclick()


if __name__ == "__main__":
    main()
