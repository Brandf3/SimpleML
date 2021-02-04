import tkinter as tk
from tkinter import filedialog
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import numpy as np

class ModelWindow:

    def clearFrame():
        for widget in frame.winfo_children():
            widget.destroy()

    def runNB(event):
        data = pd.read_csv(dataEntry.get())
        totalRows = len(data.index)
        n = totalRows // int(testSize.get())

        all_Ids = np.arange(totalRows)
        random.shuffle(all_Ids)
        test_Ids = all_Ids[0:n]
        train_Ids = all_Ids[n:]

        data_test = data.loc[test_Ids, :]
        data_train = data.loc[train_Ids, :]

        count_vect = CountVectorizer()
        X_train = count_vect.fit_transform(data_train[feature.get()])

        y_train = data_train[target.get()]
        clf = MultinomialNB()
        clf.fit(X_train, y_train)

        X_test = count_vect.transform(data_test[feature.get()])
        y_test = data_test[target.get()]
        y_predicted = clf.predict(X_test)
        
        print("Accuracy: %.2f" % accuracy_score(y_test,y_predicted))

    def fileChooser(event):
        #dataEntry = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = ("test", "*.csv"))
        dataEntry.insert(0, filedialog.askopenfilename(filetypes = [("Comma separated values", "*.csv")]))
        
    def NBForm():
        ModelWindow.clearFrame()

        innerFrame1 = tk.Frame(frame)
        text = tk.Label(innerFrame1, text="Dataset path: ")
        text.pack(side=tk.LEFT)
        
        global dataEntry
        dataEntry = tk.Entry(innerFrame1)
        dataEntry.pack(side=tk.RIGHT)
        innerFrame1.pack()

        btnFile = tk.Button(innerFrame1, text="...")
        btnFile.pack()
        btnFile.bind("<Button-1>", ModelWindow.fileChooser)

        innerFrame2 = tk.Frame(frame)
        text2 = tk.Label(innerFrame2, text="Variable to predict: ")
        text2.pack(side=tk.LEFT)
        
        global target
        target = tk.Entry(innerFrame2)
        target.pack()
        innerFrame2.pack()

        innerFrame4 = tk.Frame(frame)
        text4 = tk.Label(innerFrame4, text="Feature: ")
        text4.pack(side=tk.LEFT)
        
        global feature
        feature = tk.Entry(innerFrame4)
        feature.pack()
        innerFrame4.pack()

        innerFrame3 = tk.Frame(frame)
        text3 = tk.Label(innerFrame3, text="Test data %: ")
        text3.pack(side=tk.LEFT)

        global testSize
        testSize = tk.Entry(innerFrame3)
        testSize.insert(0, "10")
        testSize.pack()
        innerFrame3.pack()

        btn = tk.Button(frame, text="Run")
        btn.pack()
        btn.bind("<Button-1>", ModelWindow.runNB)

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
    
