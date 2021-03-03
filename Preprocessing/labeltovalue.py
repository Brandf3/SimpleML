import tkinter as tk
from tkinter import filedialog

from Preprocessing.textpreprocess import TextPreprocess
import pandas as pd
import wordsegment

class LabelToValue(TextPreprocess):

    def __init__(self, frame):
        a = TextPreprocess(self, frame)

        innerFrame = tk.Frame(frame)
        text2 = tk.Label(innerFrame, text="Words to change: ")
        text2.pack(side=tk.LEFT)
        
        self.text = tk.Text(innerFrame)
        self.text.pack(side=tk.RIGHT)
        innerFrame.pack()

    def run(self, event):
        file = open(self.dataEntry.get(), 'r')
        out = open(self.savefile.get(), 'w')

        s = file.read()
        text = str.splitlines(self.text.get("1.0", tk.END))
        for pair in text:
            index = pair.find(':')
            s = s.replace(pair[0:index], pair[index+1:])

        out.write(s)
