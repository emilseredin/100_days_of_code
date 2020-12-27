from tkinter import *


def km_to_miles():
    km = float(inp.get())
    miles = str(round(km * 1.6, 2))
    mile.config(text=miles)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=60, pady=50)

miles_label = Label(text="Miles", font=("Arial", 14))
equal_to_label = Label(text="is equal to", font=("Arial", 14))
km_label = Label(text="Km", font=("Arial", 14))
mile = Label(text="", font=("Arial", 14))
inp = Entry(width=10)
calculate = Button(text="Calculate", command=km_to_miles)

inp.grid(row=0, column=1)
miles_label.grid(row=0, column=2)
equal_to_label.grid(row=1, column=0)
mile.grid(row=1, column=1)
km_label.grid(row=1, column=2)
calculate.grid(row=2, column=1)


window.mainloop()