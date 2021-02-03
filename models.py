import tkinter as tk

class ModelWindow:

    def openNewWindow(main):
        newWindow = tk.Toplevel(main)
        text = tk.Label(newWindow, text="Please select 'File' and choose an option to get started!")
        text.pack()
        
        frame = tk.Frame(newWindow)
        frame.pack()
        test = tk.Label(frame, text="test")
        test.pack()
    
