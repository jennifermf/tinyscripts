#!/usr/bin/env python
# # -*- coding: utf-8 -*-

# quick and easy line-by-line reader for text files. I've used this for finding unique adjectives and names... it actually doesn't really have frequent use in my day-to-day life but I've been using this as my template for file-reading code. :)

import itertools
def lineReader(fname):
    word_list = []
    with open(fname) as fh:
        word_list = [[word.strip() for word in line.split() if word not in word_list] for line in fh]
        return(sorted(set(itertools.chain.from_iterable(word_list))))

fname = input("Enter file name: ")
print(lineReader(fname))
