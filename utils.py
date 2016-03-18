#!/usr/bin/python3.4
import os
import shutil

path = "./here/"
AbsolPath = "./there/"

# Add a new file
def add(path,fileName):
    shutil.copy2(os.path.join(path,fileName),os.path.join(target,fileName))

# remove all the file in the Target directory
def removeFiles(path):
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path,i)):
            os.remove(os.path.join(path, i))
        else:
            removeFiles(os.path.join(path,i)) # If you find a new directory, remove it with the files in it
    if path!=AbsolPath:
        os.rmdir(path)  # Remove directory current directory, except "root"

#removeFiles(AbsolPath)
