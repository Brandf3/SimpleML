import tkinter as tk
from tkinter import filedialog
from naivebayes import NaiveBayes
from svm import SVM
from segment import Segmentor

class ModelWindow:
        
    def nb():
        NaiveBayes(frame)

    def svm():
        SVM(frame)

    def segment():
        Segmentor(frame)
    
    def openNewWindow(main):
        newWindow = tk.Toplevel(main)
        menubar = tk.Menu(newWindow)
        
        modelmenu = tk.Menu(menubar, tearoff=0)
        modelmenu.add_command(label="Naive Bayes", command = ModelWindow.nb)
        modelmenu.add_command(label="SVM", command = ModelWindow.svm)
        menubar.add_cascade(label="Models", menu = modelmenu)

        modelmenu2 = tk.Menu(menubar, tearoff=0)
        modelmenu2.add_command(label="Hashtag Segmentor", command = ModelWindow.segment)
        menubar.add_cascade(label="Pre-processing", menu = modelmenu2)
        
        newWindow.config(menu = menubar)
        
        global frame
        frame = tk.Frame(newWindow)
        frame.pack()
                                
        text = tk.Label(frame, text="Please select 'Models' and choose an option to get started!")
        text.pack()
    
