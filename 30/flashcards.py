from tkinter import *
from tkinter import messagebox
import json


class FlashCards:

    def __init__(self):
        self.window = Tk()
        self.window.title("Flashcards")
        self.window.config(padx=50, pady=50)
        self.flashcard_bg = PhotoImage(
            file="./images/card_front.png")
        self.right_bg = PhotoImage(
            file="./images/right.png")
        self.wrong_bg = PhotoImage(
            file="./images/wrong.png")
        self.canvas = Canvas(width=800, height=526, highlightthickness=0)
        self.canvas.create_image(400, 263, image=self.flashcard_bg)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.right = Button(image=self.right_bg, highlightthickness=0)
        self.right.grid(row=1, column=1)
        self.wrong = Button(image=self.wrong_bg, highlightthickness=0)
        self.wrong.grid(row=1, column=0)

    def run(self):
        self.window.mainloop()
