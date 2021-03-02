import tkinter as tk
from tkinter import filedialog

from textpreprocess import TextPreprocess
import pandas as pd
import wordsegment

class Segmentor(TextPreprocess):

    def __init__(self, frame):
        a = TextPreprocess(self, frame)

    def run(self, event):
        wordsegment.load()
        file = open(self.dataEntry.get(), 'r')
        out = open(self.savefile.get(), 'w')
        for line in file:
            line.strip()
            lineSplit = str.split(line)
            for i in range(0, len(lineSplit)):
                if lineSplit[i][0] == '#':
                    s = wordsegment.segment(lineSplit[i][1:])
                    lineSplit[i] = " ".join(s)

            s = " ".join(lineSplit)
            out.write(s + "\n")


        

