from tkinter import *
import tkinter as tk
import tkinter.ttk
from PIL import Image, ImageTk
import sys
import os
import subprocess
import time

# location of all departments
dept_address = ["Chemical, Core 4, Right Side", "Chemistry, Core 3, Left Side", "Civil, Core 4, Left Side", "CSE, Core 2, Left Side", "Design, Core 1, Left Side", "Physics, Core 4, Right Side", "Mechanical, Core 1, Right Side", "C7", "C8", "Core 1, Right Side"]

# position variables for gui elements
Button_x = 0.5
Button_y = 0.075
Label_x = 0.5
Label_y = 0.3
Progress_Bar_x = 0.5
Progress_Bar_y = 0.5


""" tkinter window """
top = Tk()

# setting window properties
top.config(bg='thistle')
top.title("Department Locator")
top.geometry("200x200")

# initialising gui elements
var = StringVar()
label = Label(top, textvariable=var, relief=RAISED)
label2 = Text(top, height=3, width=20, bg='thistle')
label2.insert(tk.END, "Press Record button    to Search for a\n    department")

# list of images to render
render = []
for i in range(10):
    load = Image.open("AC_" + str(i) +".jpg")
    load = load.resize((375, 550), Image.ANTIALIAS)
    render.append(ImageTk.PhotoImage(load))


progress = tkinter.ttk.Progressbar(top, orient=HORIZONTAL, length=100, mode='determinate')
img = Label(top, image=render[0])

# function to update progress bar
def bar():
    for i in range(1,21):
        time.sleep(0.2)
        progress['value'] = i * 5
        top.update()
    progress['value'] = 0

def trainCallBack():
    B2.config(text="Training!!")
    B2.config(bg='red')
    top.update()
    os.system("training_module.exe")
    time.sleep(1)
    B2.config(bg='green')
    B2.config(text='Trained')
    top.update()
# Record button event handler+
def recordCallback():
    global Label_x, Label_y, Progress_Bar_y, Button_y
    B2.place(x=-1000, y=-1000)
    top.update()
    label.config(bg='green')
    var.set("Listening!!")
    label.place(relx=Label_x, rely=Label_y, anchor=CENTER)
    progress.place(relx=Progress_Bar_x, rely=Progress_Bar_y, anchor=CENTER)
    top.update()

    # invoke recording module
    subprocess.Popen("Recording_Module.exe 2 input_file.wav input_file.txt")
    bar()
    var.set("Analysing!!")
    label.config(bg='red')
    top.update()

    # invoke testing module
    os.system("identify_module.exe")

    # read result
    fin = open("res.txt")
    d = int(fin.readline()[:-1])

    # update gui
    Progress_Bar_y = 0.16
    Button_y = 0.05
    Label_y = 0.1
    progress.pack_forget()
    label2.pack_forget()
    B1.place(relx=Button_x, rely=Button_y, anchor=CENTER)
    label.place(relx=Label_x, rely=Label_y, anchor=CENTER)
    label.config(bg='cyan')
    var.set(dept_address[d])
    top.geometry("450x850")
    img.configure(image=render[d])
    img.image = render[d]
    img.place(relx=0.5, rely=0.55, anchor=CENTER)
    top.update()
    fin.close()

label2.place(relx=0.5, rely=0.7, anchor=CENTER)
B1 = Button(top, text = "Record", command = recordCallback)
B1.place(relx=Button_x, rely=Button_y, anchor=CENTER)

B2 = Button(top, text = "Train", command = trainCallBack)
B2.place(relx=Label_x, rely=Label_y, anchor=CENTER)

top.mainloop()