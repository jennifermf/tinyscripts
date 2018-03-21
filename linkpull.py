# !/usr/bin/python

# takes URL as input, outputs all links to a file
# requires the excellent pythonic HTML parser, requests_hmtl
# parser source: https://github.com/kennethreitz/requests-html

from requests_html import HTMLSession
import os, sys

def maketextfile(linklist, filename):
    with open(filename, 'a+') as file:
        for link in linklist:
            file.write(link + '\n')

def main():
    print("\nThis is a tiny link scraper!\n")
    
    # destination file for your links:
    filename = 'linklist.txt'
    
    # get URL source:
    url = input("Enter a complete URL: ")
    
    session = HTMLSession()
    r = session.get(url)
    linklist = [link for link in r.html.absolute_links]
    maketextfile(linklist, filename)
    print("\nFinished! Your file {} is located at \n {}\n".format(filename, os.getcwd()))

main()