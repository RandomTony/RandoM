#!/usr/bin/python3.4

import os
from tkinter import *
import shutil


def add(origin,fileName,target):
    shutil.copy2(os.path.join(origin,fileName),os.path.join(target,fileName))


# remove all the file in the Target directory
def removeFiles(path):
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path,i)):
            os.remove(os.path.join(path, i))
        else:
            removeFiles(os.path.join(path,i)) # If you find a new directory, remove it with the files in it
    if path!=AbsolPath:
        os.rmdir(path)  # Remove directory current directory, except "root"



def click():
    if targetEnt.get()!="" and originEnt.get()!="":
        origin = originEnt.get()
        target = targetEnt.get()
        add(origin, "hello.txt", target)


frame = Tk()

originLab = Label(frame, text="Origin").grid(row=0)
originEnt = Entry(frame)
originEnt.grid(row=0, column=1)

targetLab = Label(frame, text="Target").grid(row=1)
targetEnt = Entry(frame)
targetEnt.grid(row=1, column=1)

bouton_click = Button(frame, text="Copy", command=click).grid(row=2,column=1)
bouton_quit = Button(frame, text="Quit", command=frame.quit).grid(row=2, column=0)

frame.title("RandoM")
frame.config(width=800, height=500)
frame.mainloop()
