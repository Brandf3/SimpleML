import tkinter as tk
from tkinter import filedialog
import demoji
from textpreprocess import TextPreprocess
import pandas as pd

class Demoji(TextPreprocess):

    def __init__(self, frame):
        a = TextPreprocess(self, frame)

    def run(self, event):

        file = open(self.dataEntry.get(), 'r')
        out = open('processed.txt', 'w')
        for line in file:
            out.write(demoji.replace_with_desc(line))
        
        self.btn2.configure(state=tk.NORMAL)


        

