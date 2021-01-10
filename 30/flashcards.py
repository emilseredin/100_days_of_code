from tkinter import *
from tkinter import messagebox
import json
import csv
import random
import os


BACKGROUND = "#a9e3c6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")


class Game:

    cards, f_lang, n_lang, current_card = ([], "", "", None)

    def __init__(self):
        self.game_window = GameWindow()
        self.fc = FileController()
        Game.f_lang, Game.n_lang, Game.cards = self.fc.read()
        Game.current_card = random.choice(Game.cards)

    def run(self):
        self.game_window.show_next_card()
        self.game_window.window.mainloop()


class Card:

    def __init__(self, foreign, native):
        self.foreign = foreign
        self.native = native


class FileController:

    src = "./data/french_words.csv"
    dest = "./data/word_to_learn.csv"

    def __init__(self):
        if os.path.exists(FileController.dest):
            FileController.src = FileController.dest
        

    def read(self):
        try:
            with open(FileController.src, "r") as f:
                reader = csv.DictReader(f)
                lang_1 = reader.fieldnames[0]
                lang_2 = reader.fieldnames[1]
                return lang_1, lang_2, [Card(foreign=row["French"], native=row["English"]) for row in reader]
        except FileNotFoundError as e:
            print(e)

    def save(self, data: list, header: tuple):
        try:
            with open(FileController.dest, "w") as f:
                writer = csv.DictWriter(f, header)
                writer.writeheader()
                writer.writerows(data)
        except FileNotFoundError as e:
            print(e)


class GameWindow:

    def __init__(self):
        self.window = Tk()
        self.window.title("Flashcards")
        self.window.config(padx=50, pady=50, bg=BACKGROUND)
        self.card_front = PhotoImage(
            file="./images/card_front.png")
        self.card_back = PhotoImage(
            file="./images/card_back.png")
        self.right_bg = PhotoImage(
            file="./images/right.png")
        self.wrong_bg = PhotoImage(
            file="./images/wrong.png")
        self.canvas = Canvas(width=800, height=526,
                             highlightthickness=0, bg=BACKGROUND)
        self.card = self.canvas.create_image(400, 263)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.title = self.canvas.create_text(
            400, 150, text="", font=TITLE_FONT)
        self.word = self.canvas.create_text(400, 263, text="", font=WORD_FONT)
        self.right = Button(image=self.right_bg,
                            highlightthickness=0, borderwidth=0, command=lambda: self.button_handler("right"))
        self.right.grid(row=1, column=1)
        self.wrong = Button(image=self.wrong_bg,
                            highlightthickness=0, borderwidth=0, command=lambda: self.button_handler())
        self.wrong.grid(row=1, column=0)

    def button_handler(self, status=None):
        if status == "right":
            fc = FileController()
            header = (Game.f_lang, Game.n_lang)
            Game.cards.remove(Game.current_card)
            data = [{Game.f_lang: card.foreign, Game.n_lang: card.native}
                    for card in Game.cards]
            fc.save(data=data, header=header)
        self.window.after_cancel(self.flip_timer)
        Game.current_card = random.choice(Game.cards)
        self.show_next_card()

    def show_next_card(self):
        self.canvas.itemconfig(self.card, image=self.card_front)
        self.canvas.itemconfig(self.title, text=Game.f_lang, fill="black")
        self.canvas.itemconfig(
            self.word, text=Game.current_card.foreign, fill="black")
        self.flip_timer = self.window.after(3000, self.show_translation)

    def show_translation(self):
        self.canvas.itemconfig(self.card, image=self.card_back)
        self.canvas.itemconfig(self.title, text=Game.n_lang, fill="white")
        self.canvas.itemconfig(
            self.word, text=Game.current_card.native, fill="white")
