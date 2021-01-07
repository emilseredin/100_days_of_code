from tkinter import *
from tkinter import messagebox
import json
import os
import random
import io
# import pyperclip


class PasswordManager:

    def __init__(self):
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=20)
        self.file_controller = FileController(path="passwords.json")

    def run(self):
        self.canvas = MainCanvas()
        self.website = Label(text="Website:")
        self.website.grid(row=1, column=0, sticky="w")
        self.email = Label(text="Email:")
        self.email.grid(row=2, column=0, sticky="w")
        self.pw = Label(text="Password:")
        self.pw.grid(row=3, column=0, sticky="w")
        self.website_inp = Entry(width=24)
        self.website_inp.grid(row=1, column=1, columnspan=1, sticky="w")
        self.email_inp = Entry(width=24)
        self.email_inp.grid(row=2, column=1, columnspan=1)
        self.pw_inp = Entry(width=24)
        self.pw_inp.grid(row=3, column=1, columnspan=1, sticky="w")
        self.gen_pw = Button(text="Generate", width=7,
                             command=lambda: self.display_password(self.generate_password()))
        self.gen_pw.grid(row=3, column=2, sticky="e")
        self.add = Button(
            text="Add", width=32,
            command=self.save)
        self.add.grid(row=4, column=1, columnspan=2)
        self.search_bt = Button(text="Search", width=7, command=lambda: self.display_password(self.search()))
        self.search_bt.grid(row=1, column=2, sticky="w")
        self.website_inp.focus()
        self.email_inp.insert(0, "emil@email.com")
        self.window.mainloop()

    def save(self):
        try:
            data = self.get_data()
            website = [key for key in data][0]
        except ValueError as e:
            messagebox.showwarning(message=e)
        else:
            message = "These are the details entered\n"
            message += "Website: {}\n".format(website)
            message += "Email: {}\n".format(data[website]["email"])
            message += "Password: {}\n".format(data[website]["password"])
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
        website = self.website_inp.get().strip()
        email = self.email_inp.get().strip()
        password = self.pw_inp.get().strip()
        ok = self.validate_data((website, email, password))
        if not ok:
            raise ValueError("Empty field(s)")
        return {
            website: {
                "email": email,
                "password": password
            }
        }

    def search(self):
        website = self.website_inp.get().strip()
        if not website:
            messagebox.showinfo(message="Please enter a website")
            return
        data = self.file_controller.load()
        if not data:
            messagebox.showinfo(message="The password database does not exist")
            return
        if not website in data:
            messagebox.showinfo(message="No password stored for {}".format(website))
            return
        return data[website]["password"]
        

    def validate_data(self, data):
        for element in data:
            if not element:
                return False
        return True

    def display_password(self, value):
        if value:
            self.pw_inp.delete(0, "end")
            self.pw_inp.insert(0, value)

    def generate_password(self):
        letters_lower = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,v,u,w,x,y,z".split(
            ",")
        letters_upper = [letter.upper() for letter in letters_lower]
        numbers = [str(num) for num in range(10)]
        special = "~,@,#,$,%,^,&,*,(,),-,_,=,+,[,{,],},>,<,?".split(",")
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

    def __init__(self, path):
        self.path = path

    def load(self):
        try:
            with open(self.path, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            return {}
        else:
            return data
            

    def write(self, data):
        db = self.load()
        db.update(data)    
        with open(self.path, "w") as f:
            json.dump(db, f)
