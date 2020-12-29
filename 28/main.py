from tkinter import *
from functools import partial



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


def get_time_string(minutes, seconds):
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


def update_canvas(time):
    canvas.delete("time")
    canvas.create_text(100, 140, text=time, fill="white", font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT), tag="time")


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(main_timer)
    canvas.delete("time")
    canvas.create_text(100, 140, text="02:00", fill="white", font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT), tag="time")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def run_timer():
    minutes = 0
    seconds = 1 * 30
    global main_timer
    main_timer = window.after(0, countdown, seconds, minutes)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(seconds, minutes):
    global main_timer
    time_left = get_time_string(minutes, seconds)
    update_canvas(time_left)
    if seconds == 0:
        reset_timer()
        timer_label["text"] += CHECK
    else:
        if seconds % 60 == 0:
            minutes -= 1
        seconds -= 1
        main_timer = window.after(1000, countdown, seconds, minutes)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=60, bg=YELLOW)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35))
timer_label.grid(row=0, column=1)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_image = PhotoImage(file="./tomato.png")
# elements that can be created on canvas can overlap each other
canvas.create_image(100, 112, image=pomodoro_image)
canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT), tag="time")
canvas.grid(row=1, column=1)

start_bt = Button(
    text="Start", bg="white", fg="black", font=(FONT_NAME, 11, "bold"), 
    height=1, width=2, border=0, highlightthickness=0,
    command=run_timer
)
start_bt.grid(row=2, column=0)
reset_bt = Button(
    text="Reset", bg="white", fg="black", 
    font=(FONT_NAME, 11, "bold"), height=1, width=2, border=0, highlightthickness=0,
    command=reset_timer)
reset_bt.grid(row=2, column=2)

timer_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25))
timer_label.grid(row=3, column=1)

window.mainloop()