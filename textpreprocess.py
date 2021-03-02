import tkinter as tk
from tkinter import filedialog

class TextPreprocess:

    def __init__(self, child, frame):
        child.clearFrame(frame)

        innerFrame1 = tk.Frame(frame)
        text = tk.Label(innerFrame1, text="Dataset path: ")
        text.pack(side=tk.LEFT)
        
        child.dataEntry = tk.Entry(innerFrame1)
        child.dataEntry.pack(side=tk.RIGHT)
        innerFrame1.pack()

        btnFile = tk.Button(innerFrame1, text="...")
        btnFile.pack()
        btnFile.bind("<Button-1>", child.fileChooser)

        innerFrame2 = tk.Frame(frame)
        text2 = tk.Label(innerFrame2, text="Savefile Name: ")
        text2.pack(side=tk.LEFT)
        
        child.savefile = tk.Entry(innerFrame2)
        child.savefile.pack(side=tk.RIGHT)
        innerFrame2.pack()

        innerFrame5 = tk.Frame(frame)
        btn = tk.Button(innerFrame5, text="Run")
        btn.pack(side=tk.LEFT)
        btn.bind("<Button-1>", child.run)
        innerFrame5.pack()

    def clearFrame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def run(self, event):
        pass

    def fileChooser(self, event):
        self.dataEntry.insert(0, filedialog.askopenfilename(filetypes = [("Comma separated values", "*.csv"), ("All files", "*.*")]))

