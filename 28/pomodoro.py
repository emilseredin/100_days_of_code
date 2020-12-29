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

class MainWindow():
    
    def __init__(self, title):
        self.window = Tk()
        self.window.title(title)
        self.window.config(padx=100, pady=60, bg=YELLOW)


class Pomodoro():

    def __init__(self):
        self.window = Tk()
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=60, bg=YELLOW)
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
            command=self.reset_timer)
        self.reset_bt.grid(row=2, column=2)
        self.timer_label = Label(
            text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25))
        self.timer_label.grid(row=3, column=1)
        self.canvas = MainCanvas()
        self.timer = Timer(self.window, self.canvas, self.timer_label)
        self.window.mainloop()

    def run_timer(self):
        self.start_bt["state"] = "disabled"
        self.timer.run()

    def reset_timer(self):
        self.start_bt["state"] = "normal"
        self.timer.reset()


class MainCanvas():

    def __init__(self):
        self.canvas = Canvas(width=200, height=224,
                             bg=YELLOW, highlightthickness=0)
        self.pomodoro_image = PhotoImage(file="./tomato.png")
        self.canvas.create_image(100, 112, image=self.pomodoro_image)
        self.canvas.create_text(100, 140, text="00:00", fill="white", font=(
            FONT_NAME, FONT_SIZE, FONT_WEIGHT), tag="time")
        self.canvas.grid(row=1, column=1)

    def update_canvas(self, time: str):
        self.canvas.delete("time")
        self.canvas.create_text(100, 140, text=time, fill="white", font=(
            FONT_NAME, FONT_SIZE, FONT_WEIGHT), tag="time")


class Timer():

    def __init__(self, window, canvas, timer_label):
        self.window = window
        self.canvas = canvas
        self.timer_label = timer_label

    def run(self):
        minutes = 0
        seconds = minutes + 5
        self.main_timer = self.window.after(0, self.countdown, seconds, minutes)

    def reset(self):
        self.window.after_cancel(self.main_timer)
        self.canvas.update_canvas("02:00")

    def countdown(self, seconds, minutes):
        time_left = self.get_time_string(minutes, seconds)
        self.canvas.update_canvas(time_left)
        if seconds == 0:
            self.reset()
            self.timer_label["text"] += CHECK
        else:
            if seconds % 60 == 0:
                minutes -= 1
            seconds -= 1
            self.main_timer = self.window.after(
                1000, self.countdown, seconds, minutes)
    
    def get_time_string(self, minutes, seconds):
        seconds = seconds - minutes * 60
        time_left = ""
        if minutes < 10:
            time_left += "0"
        time_left += str(minutes)
        time_left += ":"
        if seconds < 10:
            time_left += "0"
        time_left += str(seconds)
        return time_left