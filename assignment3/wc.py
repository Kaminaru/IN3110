#!/usr/bin/env python3

import sys

def wc(filename):
    """
    Function that going through file, line by line, and prints out number of
    lines, words and characters in the file.
    In case of an error, lines, words and char will get number 404\
    """


    # holds number of characters, words and lines in the file
    lines = 0
    words = 0
    char = 0
    try: # if the file does not exist
        file = open(filename)
        for line in file: # goes through file
            lines += 1
            wordList = line.split()
            words += len(wordList)
            for el in wordList: # this way I only count characters without " "(spaces)
                char += len(el)
        file.close()
    except Exception as e:
        print(e)
        lines, words, char = 404, 404, 404

    # prints out only if there was a right file name
    print(f"{lines} {words} {char} {filename}")



if(len(sys.argv) > 1): # checks if enough arguments was given
    for i in range(1,len(sys.argv)): # using this kind of forloop, to not read
        wc(sys.argv[i])              # calling file (sys.argv[0])
    # (That works because when I write * or *.py as argument, all files that have
    #  same extension will be saved in sys.argv list.
    #  So even if * is kind of "one argument" at the end sys.argv will get more
    #  elements that is the number of the files in the directory)
else:
    print("Not enough arguments")
