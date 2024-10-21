import os
import keyboard
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
import tkinter as tk
import tkinter.font as fnt
import numpy as np
#from tinderbot import TinderBot
from analyze import image_analysis, rgb_channel, dotty, file
from detect import got
from main import my_hash, online
from offline import offline
from dependencies import dpp

app = tk.Tk()



app.geometry("470x450+500+150")

app.configure(bg='black')

app.option_add('*Font', 'Bahnschrift 9')

done = my_hash


def hashy():

    label = Label(app, text="Your Hash Code :-" +str(my_hash), bg='black', fg='white').place(relx=0.5, rely=0.9, anchor=CENTER)



#hosh = my_hash
#T.insert(tk.END, hosh)
#label.pack()
#app.update()

def trpp():
    dpp.destroy()
    app.destroy()
    while 1:
        os.system("launcher.py")
        print("Restarting...")
        exit()




label = Label(app, text="Find properties of image", bg='black', fg='white').place(relx=0.5, rely=0.04, anchor=CENTER)
A7 = tk.Button(app, text="RETRY", height=1, width=15, command=trpp, bg='#35c46e').place(relx=0.2, rely=0.1, anchor=CENTER)

A1 = Button(app, text="IMAGE PROPERTIES",height=1, width=15, command=dotty, bg='#c42f2f').place(relx=0.5, rely=0.1, anchor=CENTER)
label1 = Label(app, text="Analyzing image in RGB filter and RGB channels", bg='black', fg='white').place(relx=0.5, rely=0.24, anchor=CENTER)
A = Button(app, text="IMAGE ANALYSIS",height=1, width=15, command=image_analysis, bg='#c42f2f').place(relx=0.5, rely=0.3, anchor=CENTER)
A3 = Button(app, text="RGB CHANNEL", height=1, width=11, command=rgb_channel, bg='#7437a6').place(relx=0.8, rely=0.3, anchor=CENTER)
label2 = Label(app, text="(This option works only if the image has human face and visible)", bg='black', fg='white').place(relx=0.5, rely=0.44, anchor=CENTER)
A2 = Button(app, text="AGE AND GENDER",height=1, width=15, command=got, bg='#69a637').place(relx=0.5, rely=0.5, anchor=CENTER)
label3 = Label(app, text="Fun with image processing(for online search first you need to type \n what you need to search then click the button)", bg='black', fg='white').place(relx=0.5, rely=0.61, anchor=CENTER)
A4 = Button(app, text="GET YOUR HASH",height=1, width=15, command=hashy, bg='#a69737').place(relx=0.18, rely=0.7, anchor=CENTER)
A5 = Button(app, text="MATCH ONLINE",height=1, width=15, command=online, bg='#35c46e').place(relx=0.5, rely=0.7, anchor=CENTER)
A6 = Button(app, text="MATCH OFFLINE",height=1, width=15, command=offline, bg='#f7a840').place(relx=0.82, rely=0.7, anchor=CENTER)


out_label = tk.Label(text="Click to get your hash")
out_label.pack()


app.mainloop()
