import tkinter as tk
from tkinter import filedialog

class AbstractModel:

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
        text2 = tk.Label(innerFrame2, text="Variable to predict: ")
        text2.pack(side=tk.LEFT)
        
        child.target = tk.Entry(innerFrame2)
        child.target.pack()
        innerFrame2.pack()

        innerFrame4 = tk.Frame(frame)
        text4 = tk.Label(innerFrame4, text="Feature: ")
        text4.pack(side=tk.LEFT)
        
        child.feature = tk.Entry(innerFrame4)
        child.feature.pack()
        innerFrame4.pack()

        innerFrame3 = tk.Frame(frame)
        text3 = tk.Label(innerFrame3, text="Test data %: ")
        text3.pack(side=tk.LEFT)

        child.testSize = tk.Entry(innerFrame3)
        child.testSize.insert(0, "10")
        child.testSize.pack()
        innerFrame3.pack()

        innerFrame5 = tk.Frame(frame)
        btn = tk.Button(innerFrame5, text="Run")
        btn.pack(side=tk.LEFT)
        btn.bind("<Button-1>", child.run)

        child.btn2 = tk.Button(innerFrame5, text="Save", state=tk.DISABLED)
        child.btn2.pack(side=tk.RIGHT)
        child.btn2.bind("<Button-1>", child.save)
        innerFrame5.pack()

    def clearFrame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def run(self, event):
        pass

    def save(self, event):
        pass

    def fileChooser(self, event):
        self.dataEntry.insert(0, filedialog.askopenfilename(filetypes = [("Comma separated values", "*.csv")]))
