from tkinter import *
from PIL import Image, ImageTK

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Pepe Dame: The Game!")
        self.pack(fill = BoTH, expand = 1)
        menu = Menu(self.master)
        self.master.config(menu = menu)

        file = Menu(menu)
        file.add_command(label = "Exit", command=self.client_exit)
        file.add_command(label = "New Game", command=self.client_exit)
        menu.add_cascade(label = "File", menu = file)
        
