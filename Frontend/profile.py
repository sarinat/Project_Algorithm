from tkinter import *

class Warehouse:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg='light blue')
        self.root.title = ('WareHouse Frame')
        self.root.geometry('450x400')

        lb = Label(self.root, text='welcome to WareHouse Records', font=('arial', 20, 'bold'), fg='red')
        lb.pack(fill=X)


