# !/usr/bin/python

''' takes source and destination strings as input, and changes names of files in local directory accordingly. '''

import os, sys

def fileRename(src, dest):
    for filename in os.listdir("."):
        if src in filename:
            newname = filename.replace(src, dest)
            os.rename(filename, newname)
    return

def main():
    src = input("What is the substring you need to change? ")
    dest = input("What would you like to replace it with? ")
    fileRename(src, dest)

main()

# ls
print("New directory contents: {}".format(os.listdir(os.getcwd())))