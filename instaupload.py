import tkinter as tk
import time
from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog

class Initial(simpledialog.Dialog):
    def browseFiles(self): 
        filename1 = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Pictures", 
                                                        "*.jpg*"), 
                                                       ("All files", 
                                                        "*.*"))) 
        self.text.set(filename1)
    def browseFiles1(self): 
        filename2 = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Pictures", 
                                                        "*.jpg*"), 
                                                       ("All files", 
                                                        "*.*"))) 
        self.text1.set(filename2)

    def body(self, master):
#input fields for username and passwords
        Label(master, text="Username:").grid(row=1, column=1, sticky=W),
        Label(master, text="Password:").grid(row=2, column=1, sticky=W)
        Label(master, text="Picture path:").grid(row=4)
        Label(master, text="Captions:").grid(row=3, column=3)
        Label(master, text="Picture 2 path:").grid(row=5)
        Label(master, text="Not enough?:").grid(row=7)
        Label(master, text="Time Between Uploads in Minutes").grid(row=6)

        self.text = tk.StringVar()
        self.text.set('Enter or browse picture/path')

        self.text1 = tk.StringVar()
        self.text1.set('Enter or browse picture/path')

#input fields for tags
#Entry fields
        self.e1 = Entry(master)
        self.e2 = Entry(master)
        self.e3 = Entry(master, textvariable = self.text)
        self.e4 = Entry(master)
        self.e5 = Entry(master, textvariable = self.text1)
        self.e6 = Entry(master)
        self.e7 = Entry(master)
#Buttons
        self.b1 = Button(master, text = "Add More", bg="grey", command=self.open_additional)
        self.b1.grid(row=7, column=1, ipadx=75)

        self.b2 = Button(master, text="Browse Files", bg="blue", fg="white", command=self.browseFiles)
        self.b2.grid(row=4, column=2, ipadx=1)

        self.b3 = Button(master, text="Browse Files", bg="blue", fg="white", command=self.browseFiles1)
        self.b3.grid(row=5, column=2, ipadx=1)
#Entry field Placement
        self.e1.grid(row=1, column=1, columnspan=2, ipadx=50)
        self.e2.grid(row=2, column=1, columnspan=2, ipadx=50)
        self.e3.grid(row=4, column=1, ipadx=150)
        self.e4.grid(row=4, column=3, ipadx=150)
        self.e5.grid(row=5, column=1, ipadx=150)
        self.e6.grid(row=5, column=3, ipadx=150)
        self.e7.grid(row=6, column=1, ipadx=10, sticky=W)
#For new window
        self.tag = self.tag1 = self.tag2 = self.tag3 = self.tag4 = self.tag5 = self.tag6 = self.tag7 = None
        self.additional = None

        return self.e1
#button open page formula
    def open_additional(self):
        self.additional = Additional(self)

#input data get
    def apply(self):
        first = self.e1.get()
        second = self.e2.get()
        third = self.e3.get()
        fourth = self.e4.get()
        fif = self.e5.get()
        six = self.e6.get()
        sevnf = self.e7.get()
#variable assignment
        self.tag = (first, second, third, fourth, fif, six, sevnf)
        self.tag1 = (first)
        self.tag2 = (second)
        self.tag3 = (third)
        self.tag4 = (fourth)
        self.tag5 = (fif)
        self.tag6 = (six)
        self.tag7 = (sevnf)

#New page
class Additional(simpledialog.Dialog):
    def browseFiles2(self): 
        filename3 = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Pictures", 
                                                        "*.jpg*"), 
                                                       ("All files", 
                                                        "*.*"))) 
        self.text2.set(filename3)
    def browseFiles3(self): 
        filename4 = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Pictures", 
                                                        "*.jpg*"), 
                                                       ("All files", 
                                                        "*.*"))) 
        self.text3.set(filename4)
    def browseFiles4(self): 
        filename5 = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Pictures", 
                                                        "*.jpg*"), 
                                                       ("All files", 
                                                        "*.*"))) 
        self.text4.set(filename5)
    def browseFiles5(self): 
        filename6 = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Pictures", 
                                                        "*.jpg*"), 
                                                       ("All files", 
                                                        "*.*"))) 
        self.text5.set(filename6)

    def body(self, master):
#input fields for username and passwords
        Label(master, text="Picture 3 Path:").grid(row=2)
        Label(master, text="Captions:").grid(row=0, column=3, ipadx=150)
        Label(master, text="Picture 4 path:").grid(row=3)
        Label(master, text="Picture 5 path:").grid(row=4)
        Label(master, text="Picture 6 path:").grid(row=5)

        self.text2 = tk.StringVar()
        self.text2.set('Enter or browse picture/path')

        self.text3 = tk.StringVar()
        self.text3.set('Enter or browse picture/path')

        self.text4 = tk.StringVar()
        self.text4.set('Enter or browse picture/path')

        self.text5 = tk.StringVar()
        self.text5.set('Enter or browse picture/path')

#input fields for tags
#add as needed
        self.en1 = Entry(master, textvariable = self.text2)
        self.en2 = Entry(master)
        self.en3 = Entry(master, textvariable = self.text3)
        self.en4 = Entry(master)
        self.en5 = Entry(master, textvariable = self.text4)
        self.en6 = Entry(master)
        self.en7 = Entry(master, textvariable = self.text5)
        self.en8 = Entry(master)

        self.bn1 = Button(master, text= "Browse Files", bg="blue", fg="white", command=self.browseFiles2)
        self.bn1.grid(row=2, column=2, ipadx=1, sticky=W)

        self.bn2 = Button(master, text="Browse Files", bg="blue", fg="white", command=self.browseFiles3)
        self.bn2.grid(row=3, column=2, ipadx=1, sticky=W)

        self.bn3 = Button(master, text="Browse Files", bg="blue", fg="white", command=self.browseFiles4)
        self.bn3.grid(row=4, column=2, ipadx=1, sticky=W)

        self.bn4 = Button(master, text="Browse Files", bg="blue", fg="white", command=self.browseFiles5)
        self.bn4.grid(row=5, column=2, ipadx=1, sticky=W)

        self.en1.grid(row=2, column=1, ipadx=150)
        self.en2.grid(row=2, column=3, ipadx=150)
        self.en3.grid(row=3, column=1, ipadx=150)
        self.en4.grid(row=3, column=3, ipadx=150)
        self.en5.grid(row=4, column=1, ipadx=150)
        self.en6.grid(row=4, column=3, ipadx=150)
        self.en7.grid(row=5, column=1, ipadx=150)
        self.en8.grid(row=5, column=3, ipadx=150)

        self.ttag = self.ttag1 = self.ttag2 = self.ttag3 = self.ttag4 = self.ttag5 = self.ttag6 = self.ttag7 = self.ttag8 = None

        return self.en1 # initial focus

    def apply(self):
        fir = self.en1.get()
        sec = self.en2.get()
        thir = self.en3.get()
        fourf = self.en4.get()
        fiff = self.en5.get()
        sixx = self.en6.get()
        seve = self.en7.get()
        eigh = self.en8.get()

        self.ttag = (fir, sec, thir, fourf, fiff, sixx, seve, eigh)
        self.ttag1 = (fir)
        self.ttag2 = (sec)
        self.ttag3 = (thir)
        self.ttag4 = (fourf)
        self.ttag5 = (fiff)
        self.ttag6 = (sixx)
        self.ttag7 = (seve)
        self.ttag8 = (eigh)
#open initial window
def ut():
    root = tk.Tk()
    root.withdraw()
    d = Initial(root)
#stringify or int first page variables
    usrn = str(d.tag1)
    pasw = str(d.tag2)
    pic = str(d.tag3)
    cap = str(d.tag4)
    pic2 = str(d.tag5)
    cap2 = str(d.tag6)
    timed = int(d.tag7)
#translate minutes to seconds
    ttime = timed * 60
#stringify or int. second page variables
    if d.additional:
           pic3 = str(d.additional.ttag1)
           cap3 = str(d.additional.ttag2)
           pic4 = str(d.additional.ttag3)
           cap4 = str(d.additional.ttag4)
           pic5 = str(d.additional.ttag5)
           cap5 = str(d.additional.ttag6)
           pic6 = str(d.additional.ttag7)
           cap6 = str(d.additional.ttag8)
#countdown on terminal           
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Next Picture")
seconds = (timer * 60)

#instagram bot
bot = Bot()
bot.login(username = usrn,
    password= pasw)

bot.upload_photo(pic,
    caption = cap)
pass
countdown(seconds)

bot.upload_photo(pic2,
    caption = cap2)
pass
countdown(seconds)

bot.upload_photo(pic3,
    caption = cap3)
pass
countdown(seconds)

bot.upload_photo(pic4,
    caption = cap4)
pass
countdown(seconds)

bot.upload_photo(pic5,
    caption = cap5)
pass
countdown(seconds)

bot.upload_photo(pic6,
    caption = cap6)
pass

ut()