import tkinter as tk

class ModelWindow:
    
    def test():
        print('hello')

    def openNewWindow(main):
        newWindow = tk.Toplevel(main)
        menubar = tk.Menu(newWindow)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="test", command = ModelWindow.test)
        menubar.add_cascade(label="File", menu = filemenu)
        newWindow.config(menu = menubar)
        
        frame = tk.Frame(newWindow)
        frame.pack()
                                
        text = tk.Label(frame, text="Please select 'File' and choose an option to get started!")
        text.pack()
    
