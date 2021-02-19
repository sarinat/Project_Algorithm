from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import model.user
import Backend.connectiondb


# class Register:
class Register_Page:
    def __init__(self, root):
        self.root = root
        self.root.title('User registration')
        self.root.geometry('720x480')
        self.root.configure(bg='light grey')

        self.db=Backend.connectiondb.DBconnect()

        lbl_heading = Label(self.root, text='User Registration', bg='deep sky blue', font=('arial', 20, 'bold'))
        lbl_heading.pack(side=TOP, fill=X)
        main_frame = Frame(self.root, bd=10, relief=SUNKEN, bg='lavender')
        main_frame.place(x=80, y=80, width=450, height=200)
        lbl_uname = Label(main_frame, text='User Name', font=('arial', 15, 'bold'), \
                          bg='lavender', fg='blue')
        lbl_uname.grid(row=0, column=0, padx=8, pady=10)
        self.ent_uname = Entry(main_frame, font=('arial', 15, 'bold'))
        self.ent_uname.grid(row=0, column=1, padx=8, pady=10)
        lbl_password = Label(main_frame, text='Password', font=('arial', 15, 'bold'), \
                             bg='lavender', fg='blue')
        lbl_password.grid(row=1, column=0, padx=8, pady=10)
        self.ent_password = Entry(main_frame, font=('arial', 15, 'bold'))
        self.ent_password.grid(row=1, column=1, padx=8, pady=10)
        lbl_add = Label(main_frame, text='Address', font=('arial', 15, 'bold'), \
                        bg='lavender', fg='blue')
        lbl_add.grid(row=2, column=0, padx=8, pady=10)
        self.ent_add = Entry(main_frame, font=('arial', 15, 'bold'))
        self.ent_add.grid(row=2, column=1, padx=8, pady=10)
        lbl_cmb = Label(main_frame, text='Gender', font=('arial', 15, 'bold'), \
                        background='lavender', fg='blue')
        lbl_cmb.grid(row=3, column=0)
        self.cmb_gender = ttk.Combobox(main_frame, font=('arial', 15, 'bold'))
        self.cmb_gender['values'] = ('Male', 'Female', 'Others')
        self.cmb_gender.grid(row=3, column=1)
        btn_frame = Frame(self.root, bd=5, relief=GROOVE, bg='deep sky blue')
        btn_frame.place(x=100, y=300, width=400, height=60)
        btn_register = Button(btn_frame, text='Register', font=('arial', 15, 'bold'), width=8, bd=5, relief=GROOVE, \
                              command=self.add_click, padx=5)
        btn_register.place(x=50)
        btn_reset = Button(btn_frame, text='Reset', font=('arial', 15, 'bold'), width=8, bd=5, relief=GROOVE, padx=5)
        btn_reset.place(x=220)

    def reset_click(self):
        self.ent_uname.delete(0, END)
        self.ent_password.delete(0, END)
        self.ent_add.delete(0, END)
        self.ent_uname.insert(0, '')
        self.ent_password.insert(0, '')
        self.ent_add.insert(0, '')

    def add_click(self):
        username = self.ent_uname.get()
        password = self.ent_password.get()
        add = self.ent_add.get()
        # gender=self.cmb_gender.current()
        gender = self.cmb_gender.get()
        if username == '' or password == '' or add == '' or gender == '':
            messagebox.showerror('Error', 'plz fill the empty field')
            return

        U = model.user.User(username,password,add,gender)

        query = "insert into user(Username,Password,Address,Gender) values(%s,%s,%s,%s)"
        values=(U.get_username(),U.get_password(),U.get_address(),U.get_gender())

        self.db.insert(query,values)

        messagebox.showinfo('Success', 'User Registration successful')
        self.root.destroy()
