#!/usr/bin/python3.4

import os
from tkinter import *
import shutil
from tkinter.filedialog import askdirectory

class RandoM:

    def __init__(self):
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
    def removeFiles(self,path):
        for i in os.listdir(path):
            if os.path.isfile(os.path.join(path,i)):
                os.remove(os.path.join(path, i))
            else:
                removeFiles(os.path.join(path,i)) # If you find a new directory, remove it with the files in it
        if path!=AbsolPath:
            os.rmdir(path)  # Remove directory current directory, except "root"

    def countFile(self,path):
        k = 0
        for i in os.listdir(path):
            if os.path.isfile(os.path.join(path,i)):
                k += 1
            else:
                k+= self.countFile(os.path.join(path,i))
        return k

    def copyAll(self,path):
        for i in os.listdir(path):
            if path!=self.targetEnt.get() and os.path.isfile(os.path.join(path,i)):
                print(os.path.join(path,i))
                self.add(path,i, self.targetEnt.get())
            elif os.path.isdir(os.path.join(path,i)):
                self.copyAll(os.path.join(path,i))

    def copyRandom(self):
        pass

    def click(self):
        if os.path.exists(self.targetEnt.get()) and os.path.exists(self.originEnt.get()):
            origin = self.originEnt.get()
            target = self.targetEnt.get()
            print(self.numberEntry.get())
            #self.add(origin, "hello.txt", target)
            if self.countFile(origin)<=int(self.numberEntry.get()):
                self.copyAll(self.originEnt.get())
            else:
                self.copyRandom()

app = RandoM()
