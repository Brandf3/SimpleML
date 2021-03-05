import tkinter as tk
from PIL import ImageTk, Image
import webbrowser
from models import ModelWindow

class Main:
    def __init__(self):
        self.modelWindow = ModelWindow()
    
    def open_model_window(self, event):
        self.modelWindow.openNewWindow(self.window)
        
    def github_press(self, event):
        webbrowser.open("https://github.com/Brandf3/SimpleML")   

    def discord_press(self, event):
        webbrowser.open("https://discord.gg/ck73548dph")
        
    def main(self):
        self.window = tk.Tk()
        intro = tk.Label(text="Welcome to SimpleML")
        intro.pack()

        canvas = tk.Canvas(self.window, width = 500, height = 300)
        canvas.pack()
        img = ImageTk.PhotoImage(Image.open("logo.png"))
        canvas.create_image(20, 20, anchor='nw', image=img)

        btn = tk.Button(text="Get started")
        btn.pack(side=tk.LEFT)
        btn.bind("<Button-1>", self.open_model_window)

        btn2 = tk.Button(text="Github")
        btn2.pack(side=tk.LEFT)
        btn2.bind("<Button-1>", self.github_press)

        btn3 = tk.Button(text="Discord")
        btn3.pack(side=tk.LEFT)
        btn3.bind("<Button-1>", self.discord_press)

        self.window.mainloop()

driver = Main()
driver.main()
