from game_data import data
from art import vs, logo
import random
import os


class Game():

    def __init__(self):
        random.shuffle(data)
        self.data = data
        self.player = {"score": 0}
        self.a = data.pop()
        self.b = data.pop()

    def clear(self):
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    def check_answer(self):
        guess = input(
            "Who has more followers? Type 'A' or 'B': ").strip().upper()
        answer = 'A' if self.a["follower_count"] > self.b["follower_count"] else 'B'
        return guess == answer

    def print_choices(self):
        message = "{} {}: {}, a {}, from {}."
        print(message.format("Compare", "A",
                             self.a["name"], self.a["description"], self.a["country"]))
        print(vs)
        print(message.format("Against", "B",
                             self.b["name"], self.b["description"], self.b["country"]))

    def play(self):
        keep_going = True
        print(logo)
        while keep_going:
            self.print_choices()
            is_correct = self.check_answer()
            self.clear()
            print(logo)
            if len(data) == 0:
                keep_going = False
                print("This is it for now. You guessed everything right!")
            elif not is_correct:
                keep_going = False
                print("Sorry, that's wrong. Final score: {}".format(
                    self.player["score"]))
            else:
                self.player["score"] += 1
                self.a = self.b
                self.b = data.pop()
                print("You're right! Current score: {}".format(
                    self.player["score"]))
