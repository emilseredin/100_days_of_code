import tkinter


def button_clicked():
    new_text = inp.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("Test")
window.minsize(width=480, height=480)
window.config(padx=50, pady=50)

# label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# pack centers (by default) the element on the screen
# places elements one after another
# difficult to specify th precise position
# one of the layout managers
# others are place (precise positioning) an grid
# my_label.pack(side="left")
my_label.grid(column=2, row=0)

# my_label["text"] = "New Text"
my_label.config(text="New Text")

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=0, row=1)

inp = tkinter.Entry(width=10)
inp.grid(column=1, row=1)

button = tkinter.Button(text="BUTTon", command=button_clicked)
button.grid(column=0, row=2)

window.mainloop()
