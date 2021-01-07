from tkinter import *
from tkinter import messagebox
import csv
import os
import random
# import pyperclip


class PasswordManager:

    def __init__(self):
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=20)
        self.file_controller = FileController()

    def run(self):
        self.canvas = MainCanvas()
        self.website = Label(text="Website:")
        self.website.grid(row=1, column=0, sticky="w")
        self.email = Label(text="Email:")
        self.email.grid(row=2, column=0, sticky="w")
        self.pw = Label(text="Password:")
        self.pw.grid(row=3, column=0, sticky="w")
        self.website_inp = Entry(width=35)
        self.website_inp.grid(row=1, column=1, columnspan=2)
        self.email_inp = Entry(width=35)
        self.email_inp.grid(row=2, column=1, columnspan=2)
        self.pw_inp = Entry(width=21)
        self.pw_inp.grid(row=3, column=1, columnspan=2, sticky="w")
        self.gen_pw = Button(text="Generate", width=7,
                             command=self.display_password)
        self.gen_pw.grid(row=3, column=2, sticky="e")
        self.add = Button(
            text="Add", width=32,
            command=self.save)
        self.add.grid(row=4, column=1, columnspan=2)
        self.website_inp.focus()
        self.email_inp.insert(0, "emil@email.com")
        self.window.mainloop()

    def save(self):
        try:
            data = self.get_data()
        except ValueError as e:
            messagebox.showwarning(message=e)
        else:
            message = "These are the details entered\n"
            message += "Website: {}\n".format(data["website"])
            message += "Email: {}\n".format(data["email"])
            message += "Password: {}\n".format(data["password"])
            is_ok = messagebox.askokcancel(message=message)
            if is_ok:
                try:
                    self.file_controller.write(data)
                except Exception as e:
                    messagebox.showwarning(message="Something went wrong")
                    print(e)
                else:
                    self.pw_inp.delete(0, "end")
                    self.website_inp.delete(0, "end")
                    messagebox.showinfo(message="Password has been added")

    def get_data(self):
        data = {
            "website": self.website_inp.get().strip(),
            "email": self.email_inp.get().strip(),
            "password": self.pw_inp.get().strip()
        }
        ok = self.validate_data(data)
        if not ok:
            raise ValueError("Empty field(s)")
        return data

    def validate_data(self, data):
        for key, value in data.items():
            if not value:
                return False
        return True

    def display_password(self):
        pw = self.generate_password()
        self.pw_inp.delete(0, "end")
        self.pw_inp.insert(0, pw)

    def generate_password(self):
        letters_lower = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,v,u,w,x,y,z".split(
            ",")
        letters_upper = [letter.upper() for letter in letters_lower]
        numbers = [str(num) for num in range(10)]
        special = []
        with open("special_characters.txt") as f:
            for line in f.readlines():
                special.append(line.strip())
        chars = letters_lower + letters_upper + numbers + special
        random.shuffle(chars)
        return "".join(chars[:16])


class MainCanvas():

    def __init__(self):
        self.canvas = Canvas(width=200, height=189, highlightthickness=0)
        self.pomodoro_image = PhotoImage(file="./logo.png")
        self.canvas.create_image(100, 95, image=self.pomodoro_image)
        self.canvas.grid(row=0, column=1)


class FileController:

    def __init__(self):
        self.fieldnames = ["website", "email", "password"]
        self.path = "passwords.csv"

    def write(self, data):
        if not os.path.exists(self.path):
            self.initialize_file()
        with open(self.path, "a") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writerow(data)

    def initialize_file(self):
        with open(self.path, "w") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
