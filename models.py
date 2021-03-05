import tkinter as tk
from tkinter import filedialog
from TextModels.naivebayes import NaiveBayes
from TextModels.svm import SVM
from Preprocessing.segment import Segmentor
from Preprocessing.labeltovalue import LabelToValue

class ModelWindow:
    def __init__(self):
        pass
        
    def nb(self):
        NaiveBayes(self.frame)

    def svm(self):
        SVM(self.frame)

    def segment(self):
        Segmentor(self.frame)

    def labeltovalue(self):
        LabelToValue(self.frame)
    
    def openNewWindow(self, main):
        newWindow = tk.Toplevel(main)
        menubar = tk.Menu(newWindow)
        
        modelmenu = tk.Menu(menubar, tearoff=0)
        modelmenu.add_command(label="Naive Bayes", command = self.nb)
        modelmenu.add_command(label="SVM", command = self.svm)
        menubar.add_cascade(label="Models", menu = modelmenu)

        modelmenu2 = tk.Menu(menubar, tearoff=0)
        modelmenu2.add_command(label="Hashtag Segmentor", command = self.segment)
        modelmenu2.add_command(label="Labels to Values", command = self.labeltovalue)
        menubar.add_cascade(label="Pre-processing", menu = modelmenu2)
        
        newWindow.config(menu = menubar)
        
        self.frame = tk.Frame(newWindow)
        self.frame.pack()
                                
        text = tk.Label(self.frame, text="Please select 'Models' and choose an option to get started!")
        text.pack()
    
