import tkinter as tk
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import numpy as np
from TextModels.abstractmodel import AbstractModel

class NaiveBayes(AbstractModel):

    def __init__(self, frame):
        a = AbstractModel(self, frame)

    def run(self, event):

        data = pd.read_csv(self.dataEntry.get())
        totalRows = len(data.index)
        n = totalRows // int(self.testSize.get())

        all_Ids = np.arange(totalRows)
        random.shuffle(all_Ids)
        test_Ids = all_Ids[0:n]
        train_Ids = all_Ids[n:]

        data_test = data.loc[test_Ids, :]
        data_train = data.loc[train_Ids, :]

        count_vect = CountVectorizer()
        X_train = count_vect.fit_transform(data_train[self.feature.get()])

        y_train = data_train[self.target.get()]
        clf = MultinomialNB()
        clf.fit(X_train, y_train)

        X_test = count_vect.transform(data_test[self.feature.get()])
        y_test = data_test[self.target.get()]
        y_predicted = clf.predict(X_test)

        self.btn2.configure(state=tk.NORMAL)
        print("Accuracy: %.2f" % accuracy_score(y_test,y_predicted))

        
