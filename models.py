import tkinter as tk
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

class ModelWindow:

    def clearFrame():
        for widget in frame.winfo_children():
            widget.destroy()

    def runNB():
        data = pd.read_csv(dataEntry)
        
        
    def NBForm():
        ModelWindow.clearFrame()

        innerFrame1 = tk.Frame(frame)
        text = tk.Label(innerFrame1, text="Dataset path: ")
        text.pack(side=tk.LEFT)
        
        global dataEntrys
        dataEntry = tk.Entry(innerFrame1)
        dataEntry.pack(side=tk.RIGHT)
        innerFrame1.pack()
        
        global target
        target = tk.Entry(frame)
        target.insert(0, "Variable to predict")
        target.pack()

        global testSize
        testSize = tk.Entry(frame, state='disabled')
        testSize.insert(0, "10%")
        testSize.pack()
        

    def openNewWindow(main):
        newWindow = tk.Toplevel(main)
        menubar = tk.Menu(newWindow)
        modelmenu = tk.Menu(menubar, tearoff=0)
        modelmenu.add_command(label="Naive Bayes", command = ModelWindow.NBForm)
        menubar.add_cascade(label="Models", menu = modelmenu)
        newWindow.config(menu = menubar)
        
        global frame
        frame = tk.Frame(newWindow)
        frame.pack()
                                
        text = tk.Label(frame, text="Please select 'Models' and choose an option to get started!")
        text.pack()
    
