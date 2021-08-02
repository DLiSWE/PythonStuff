import tkinter as tk
from tkinter import *
from tkinter import simpledialog
from uploadtest import *
from instaquickstart import *
from Gsheet_V2 import *

class Home(simpledialog.Dialog):
    def changeColor1(self):
        self.b1["bg"]="blue"
        self.b1["fg"]="yellow"

    def changeColor2(self):
        self.b2["bg"]="blue"
        self.b2["fg"]="yellow"

    def body(self, master):
#input fields for username and passwords
        Label(master, text="Social Media Scripts").grid(row=1, column=1),
        Label(master, text="Google Apps Scripts").grid(row=1, column=2, ipadx=100)
        Label(master, text=" ").grid(row=3, column=2, ipady=10)
#Buttons
        self.utz = ut
        self.b1 = Button(master, text = "Insta-Upload", bg="magenta", fg="RoyalBlue4", command=lambda:[self.utz()])
        self.b1.grid(row=2, column=1)

        self.osha = bosh
        self.b2 = Button(master, text = "Insta-Bot", bg="magenta", fg="RoyalBlue4", command=lambda:[self.osha()])
        self.b2.grid(row=3, column=1)

        self.gsht = gshtda
        self.b3 = Button(master, text = "Google Sheets Supermetrics Data Analysis", bg="dark green", fg="white", command=lambda:[self.gsht()])
        self.b3.grid(row=2, column=2)

root = tk.Tk()
root.title("Home")
root.withdraw()
e = Home(root)
#stringify or int first page variables
