import random
from art import logo


def play():
    levels = {"easy": 10, "hard": 5}
    difficulty = input(
        "Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
    num = random.randint(1, 100)
    i = levels[difficulty]
    guess = 0
    keep_running = True
    while keep_running:
        if i == 0:
            print("You've run out of guesses, you lose. The answer was {}.".format(num))
            keep_running = False
        else:
            print("You have {} attempts remaining to guess the number.".format(i))
            guess = int(input("Make a guess: "))
            if guess == num:
                print("You got it! The answer was {}.".format(guess))
                keep_running = False
            else:
                i = i - 1
                message = "Too low." if guess < num else "Too high."
                message += "\nGuess again." if i > 0 else ""
                print(message)


def main():
    print(logo)
    print("Welcome to the Number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    play()


if __name__ == "__main__":
    main()
