from tkinter import *


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
FONT_SIZE = 25
FONT_WEIGHT = "bold"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = "✓"


class Pomodoro():

    def __init__(self):
        self.window = Tk()
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=60, bg=YELLOW)
        self.completed = 0
        self.state = "work"

    def run(self):
        self.timer_label = Label(
            text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35))
        self.timer_label.grid(row=0, column=1)
        self.start_bt = Button(
            text="Start", bg="white", fg="black", font=(FONT_NAME, 11, "bold"),
            height=1, width=2, border=0, highlightthickness=0,
            command=self.run_timer)
        self.start_bt.grid(row=2, column=0)
        self.reset_bt = Button(
            text="Reset", bg="white", fg="black",
            font=(FONT_NAME, 11, "bold"), height=1, width=2, border=0, highlightthickness=0,
            command=self.reset_timer, state="disabled")
        self.reset_bt.grid(row=2, column=2)
        self.timer_label = Label(
            text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25))
        self.timer_label.grid(row=3, column=1)
        self.canvas = MainCanvas()
        self.timer = Timer(self)
        self.window.mainloop()

    def run_timer(self):
        self.reset_bt["state"] = "normal"
        self.start_bt["state"] = "disabled"
        if self.state == "work":
            self.timer.run(minutes=WORK_MIN)
        else:
            if self.completed % 4 == 0:
                self.timer.run(minutes=LONG_BREAK_MIN)
            else:
                self.timer.run(minutes=SHORT_BREAK_MIN)

    def reset_timer(self):
        self.reset_bt["state"] = "disabled"
        self.start_bt["state"] = "normal"
        self.window.after_cancel(self.timer.main_timer)
        if self.state == "work":
            text = "{}:00".format(WORK_MIN)
            self.canvas.update_canvas(text)
        else:
            if self.completed % 4 == 0:
                text = "{}:00".format(LONG_BREAK_MIN)
                self.canvas.update_canvas(text)
            else:
                text = "{}:00".format(SHORT_BREAK_MIN)
                self.canvas.update_canvas(text)

    def toggle_state(self):
        if self.state == "work":
            self.state = "break"
        else:
            self.state = "work"


class MainCanvas():

    def __init__(self):
        self.canvas = Canvas(width=200, height=224,
                             bg=YELLOW, highlightthickness=0)
        self.pomodoro_image = PhotoImage(file="./tomato.png")
        self.canvas.create_image(100, 112, image=self.pomodoro_image)
        self.timer_text = self.canvas.create_text(100, 140, text="25:00", fill="white", font=(
            FONT_NAME, FONT_SIZE, FONT_WEIGHT), tag="time")
        self.canvas.grid(row=1, column=1)

    def update_canvas(self, time: str):
        self.canvas.itemconfig(self.timer_text, text=time)


class Timer():

    def __init__(self, pomodoro):
        self.pomodoro = pomodoro

    def run(self, minutes):
        self.seconds = minutes * 60
        self.main_timer = self.pomodoro.window.after(0, self.countdown)

    def countdown(self):
        time_left = self.get_time_string()
        self.pomodoro.canvas.update_canvas(time_left)
        if self.seconds == 0:
            if self.pomodoro.state == "work":
                self.pomodoro.timer_label["text"] += CHECK
                self.pomodoro.completed += 1
            self.pomodoro.toggle_state()
            self.pomodoro.reset_timer()
        else:
            self.seconds -= 1
            self.main_timer = self.pomodoro.window.after(
                1000, self.countdown)

    def get_time_string(self):
        minutes = self.seconds // 60
        seconds = self.seconds % 60
        if minutes < 10:
            minutes = "0{}".format(minutes)
        if seconds < 10:
            seconds = "0{}".format(seconds)
        return "{}:{}".format(minutes, seconds)
