#!/usr/bin/python3.4

import os
from tkinter import *
import shutil
from tkinter.filedialog import askdirectory
from random import random


class RandoM:

    def __init__(self):

        self.extensions = ["flac", "mp3"]

        self.frame = Tk()
        self.originText = StringVar()
        self.originLab = Label(self.frame, text="Origin").grid(row=0)
        self.originEnt = Entry(self.frame, textvariable=self.originText)
        self.originEnt.grid(row=0, column=1)
        self.originBut = Button(self.frame, text="|", command=self.setOrigin).grid(row=0,column=2)

        self.targetText = StringVar()
        self.targetLab = Label(self.frame, text="Target").grid(row=1)
        self.targetEnt = Entry(self.frame, textvariable=self.targetText)
        self.targetEnt.grid(row=1, column=1)
        self.targetBut = Button(self.frame, text="|", command=self.setTarget).grid(row=1,column=2)

        self.numberText = StringVar()
        self.numberLab = Label(self.frame, text="Number of music").grid(row=2, column=0)
        self.numberEntry = Entry(self.frame,textvariable=self.numberText,width="10")
        self.numberEntry.grid(row=2, column=1)

        self.bouton_click = Button(self.frame, text="Start", command=self.click).grid(row=2,column=2)
        self.bouton_quit = Button(self.frame, text="Quit", command=self.frame.quit).grid(row=4, column=0)

        self.stat = StringVar()
        self.stat.set("Waiting ... ")
        self.statLab = Label(self.frame, textvariable=self.stat)
        self.statLab.grid(row = 3)

        self.frame.title("RandoM")
        self.frame.config(width=800, height=500)
        self.frame.mainloop()

    def getDir(self,entryText):
        entryText.set(askdirectory())

    def setOrigin(self):
        self.getDir(self.originText)

    def setTarget(self):
        self.getDir(self.targetText)

    def add(self,origin,fileName,target):
        shutil.copy2(os.path.join(origin,fileName),os.path.join(target,fileName))


    # remove all the file in the Target directory
    def remove_files(self,path):
        for i in os.listdir(path):
            if os.path.isfile(os.path.join(path,i)):
                os.remove(os.path.join(path, i))
            else:
                self.remove_files(os.path.join(path,i)) # If you find a new directory, remove it with the files in it
        if path != self.targetEnt.get():
            os.rmdir(path)  # Remove directory current directory, except "root"

    def count_file(self,path):
        k = 0
        for i in os.listdir(path):
            if path != self.targetEnt.get() and os.path.isfile(os.path.join(path,i)) and i.split(".")[-1] in self.extensions:
                k += 1
            elif os.path.isdir(os.path.join(path, i )):
                k += self.count_file(os.path.join(path,i))
        return k

    def list_file(self, path):
        music = []
        for i in os.listdir(path):
            if path != self.targetEnt.get() and os.path.isfile(os.path.join(path, i)) and i.split(".")[-1] in self.extensions:
                music.append(os.path.join(path, i))
            elif os.path.isdir(os.path.join(path, i)):
                music.extend(self.list_file(os.path.join(path, i)))
        return music

    def copyAll(self, path):
        for i in os.listdir(path):
            if path!=self.targetEnt.get() and os.path.isfile(os.path.join(path,i)):
                self.stat.set(i)
                self.add(path,i, self.targetEnt.get())
            elif os.path.isdir(os.path.join(path,i)):
                self.copyAll(os.path.join(path,i))
        if path!=self.targetEnt.get():
            self.stat.set("Done.")

    def copyRandom(self):
        music = self.list_file(self.originEnt.get())
        for i in range(int(self.numberEntry.get())):
            n = int(random()*len(music))
            self.stat.set(os.path.basename(music[n]))
            self.add(os.path.dirname(music[n]), os.path.basename(music[n]), self.targetEnt.get())
            music.remove(music[n])
        self.stat.set("Done.")

    def click(self):
        if os.path.exists(self.targetEnt.get()) and os.path.exists(self.originEnt.get()):
            origin = self.originEnt.get()

            self.stat.set("Removing files ...")
            self.remove_files(self.targetEnt.get())

            self.stat.set("Counting files ...")
            if self.count_file(origin) <= int(self.numberEntry.get()):
                self.copyAll(self.originEnt.get())
            else:
                self.copyRandom()

app = RandoM()
