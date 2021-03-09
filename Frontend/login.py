from tkinter import *
from tkinter import messagebox
import Frontend.register
import Backend.connectiondb
import Frontend.profile
from PIL import ImageTk, Image
import datetime

date = datetime.datetime.now().date()


class My_Login:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg='light grey')
        self.root.title("Warehouse Login Page")
        self.root.geometry('1350x900')

        self.db=Backend.connectiondb.DBconnect()

        lbl_head=Label(self.root, text='WareHouse Login', bd=5, bg='deep sky blue', font=('Italic',20,'bold'))
        lbl_head.pack(side=TOP,fill=X)

        global logo
        logo = ImageTk.PhotoImage(Image.open("E:\picture\Warehouse1234.jpg"))
        logo1 = Label(self.root, image=logo)
        logo1.place(x=0, y=0)

        self.date_l = Label(logo1, text="Today's Date: " + str(date), font=('arial', 20, 'bold'), fg='black', bg='pink')
        self.date_l.place(x=1000, y=5)

        self.label1 = Label(logo1, bg="pink", text="WELCOME TO NEPAL WAREHOUSE LOGIN",
                            font=('Times New Roman', 25, 'bold'))
        self.label1.place(x=50, y=80)

        self.label1 = Label(logo1, bg="pink", text="Please proceed!",
                            font=('Times New Roman', 25, 'bold'))
        self.label1.place(x=240, y=140)

        main_frame=Frame(self.root, bd=10, relief=SUNKEN, bg='lavender')
        main_frame.place(x=150,y=200, width=450,height=150)

        lbl_username=Label(main_frame, text='User Name',bg='lavender',fg='blue', font=('arial',18,'bold'))
        lbl_username.grid(row=0, column=0,padx=10,pady=10)

        self.ent_username=Entry(main_frame, font=('arial',15,'bold'))
        self.ent_username.grid(row=0, column=1,padx=10, pady=10)

        lbl_password = Label(main_frame, text='Password', bg='lavender', fg='blue', font=('arial', 18, 'bold'))
        lbl_password.grid(row=1, column=0, padx=10, pady=10)

        self.ent_password = Entry(main_frame, font=('arial', 15, 'bold'), show="********")
        self.ent_password.grid(row=1, column=1, padx=10, pady=10)

        frame_btn = Frame(self.root, bd=5, relief=GROOVE, bg='white')
        frame_btn.place(x=180, y=360, width=390, height=60)

        btn_login = Button(frame_btn, text="Login", font=('arial', 16, 'bold'),bg='deep sky blue', bd=3, command=self.btn_login_click)
        btn_login.place(x=50, y=5)
        btn_reset = Button(frame_btn, text="Reset", font=('arial', 16, 'bold'),bg = 'deep sky blue', bd=3, command=self.btn_reset_click)
        btn_reset.place(x=240, y=5)

        lbl_signup = Label(self.root, text='Are you a new user? Sign-up here!', fg='black',relief=GROOVE,
                           bg='white', bd= 3,font=('arial', 20, 'bold'))
        lbl_signup.place(x=150, y=450)
        lbl_signup.bind('<Button-1>', self.lbl_signup_click)

        exit_button = Button(self.root, text="EXIT", font=('arial', 16, 'bold'), bg='red', width=5, bd=4, command=self.pExit)
        exit_button.place(x=320, y=550, width=100, height=50)


    def btn_reset_click(self):
        self.ent_username.delete(0, END)
        self.ent_username.insert(0, "")
        self.ent_password.delete(0, END)
        self.ent_password.insert(0, "")

    def btn_login_click(self):
        uname = self.ent_username.get()
        passw = self.ent_password.get()

        if uname == '' or passw == '':
            messagebox.showerror('Error', 'Please field the empty field')
        else:
            query ="Select * from user where Username=%s and Password=%s"
            values=(uname,passw)
            rows = self.db.select(query, values)

            data=[]

            if len(rows)!=0:
                for row in rows:
                    data.append(row[1])
                    data.append(row[2])
                print(data)
                if uname==data[0] and passw==data[1]:
                    self.btn_reset_click()
                    # messagebox.showinfo("Login success")
                    tk=Tk()
                    Frontend.profile.Warehouse(tk)
                    self.root.destroy()
                else:
                    messagebox.showerror(('Error', 'INVALID username or password'))

            else:
                messagebox.showinfo('please register first')


    def lbl_signup_click(self, event):
        tk = Tk()
        Frontend.register.Register_Page(tk)

    def pExit(self):
        self.root.destroy()


#window=Tk()
#My_Login(window)
#window.mainloop()