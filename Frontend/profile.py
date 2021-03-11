from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Backend import connectiondb
import model.product
import model.searchnsort
import Frontend.login


class Warehouse:
    def __init__(self, root):
        self.root = root
        self.root.config(bg='grey')
        self.root.title('Inventory WareHouse Records')
        self.root.geometry('1350x700')

        self.db = connectiondb.DBconnect()
        self.pid=StringVar()
        self.pname=StringVar()
        self.pprice=StringVar()
        self.pqu=StringVar()
        self.pman=StringVar()
        self.pcont=StringVar()
        self.Search=StringVar()
        self.Sort=StringVar()


        ititle=Label(self.root,text='NEPAL WAREHOUSE INVENTORY MANAGEMENT SYSTEM',bd=5, relief=GROOVE,
                    font=('arial', 35, 'bold'), bg="deep sky blue")
        ititle.pack(side=TOP, fill=X)

    #================ Manage Frame===============================

        LeftFrame=Frame(self.root, bd=4, relief=RIDGE, bg='lavender')
        LeftFrame.place(x=30, y=100, width=450, height=560)

        Lefttitle=Label(LeftFrame, text="Product Information", font=('arial', 20, 'bold'), bg='lavender')
        Lefttitle.grid(row=0, columnspan=2, pady=20)

        lbl_id=Label(LeftFrame, text="Product ID", font=('arial', 15, 'bold'), bg='lavender')
        lbl_id.grid(row=1, column=0, pady=10, padx=10, sticky='w')

        self.txt_id=Entry(LeftFrame, font=('arial', 15, 'bold'),relief=GROOVE, bd=5,textvariable=self.pid)
        self.txt_id.grid(row=1, column=1, pady=10, padx=10, sticky='w')

        lbl_name = Label(LeftFrame, text="Product Name", font=('arial', 15, 'bold'), bg='lavender')
        lbl_name.grid(row=2, column=0, pady=10, padx=10, sticky='w')

        self.txt_name = Entry(LeftFrame, font=('arial', 15, 'bold'), relief=GROOVE, bd=5)
        self.txt_name.grid(row=2, column=1, pady=10, padx=10, sticky='w')

        lbl_price = Label(LeftFrame, text="Product Price", font=('arial', 15, 'bold'), bg='lavender')
        lbl_price.grid(row=3, column=0, pady=10, padx=10, sticky='w')

        self.txt_price = Entry(LeftFrame, font=('arial', 15, 'bold'), relief=GROOVE, bd=5)
        self.txt_price.grid(row=3, column=1, pady=10, padx=10, sticky='w')

        lbl_quantity = Label(LeftFrame, text="Product Quantity", font=('arial', 15, 'bold'), bg='lavender')
        lbl_quantity.grid(row=4, column=0, pady=10, padx=10, sticky='w')

        self.txt_quantity = Entry(LeftFrame, font=('arial', 15, 'bold'), relief=GROOVE, bd=5)
        self.txt_quantity.grid(row=4, column=1, pady=10, padx=10, sticky='w')

        lbl_manufacture = Label(LeftFrame, text="Manufacturer", font=('arial', 15, 'bold'), bg='lavender')
        lbl_manufacture.grid(row=5, column=0, pady=10, padx=10, sticky='w')

        self.txt_manufacture = Entry(LeftFrame, font=('arial', 15, 'bold'), relief=GROOVE, bd=5)
        self.txt_manufacture.grid(row=5, column=1, pady=10, padx=10, sticky='w')

        lbl_contact = Label(LeftFrame, text="Company Contact", font=('arial', 15, 'bold'), bg='lavender')
        lbl_contact.grid(row=6, column=0, pady=10, padx=10, sticky='w')

        self.txt_contact = Entry(LeftFrame, font=('arial', 15, 'bold'), relief=GROOVE, bd=5)
        self.txt_contact.grid(row=6, column=1, pady=10, padx=10, sticky='w')

    #====================Button Frame=====================
        btn_Frame=Frame(LeftFrame, bd=3, bg='lavender', relief=RIDGE)
        btn_Frame.place(x=10, y=420, width=420)

        add_button=Button(btn_Frame, text="ADD", font=('arial', 12, 'bold'),bg = 'deep sky blue',width=10, bd=5,command=self.add_info)
        add_button.grid(row=0, column=0, padx=10, pady=10)

        update_button = Button(btn_Frame, text="UPDATE",font=('arial', 12, 'bold'),bg = 'deep sky blue', width=10, bd=5, command=self.update_data)
        update_button.grid(row=0, column=2, padx=10, pady=10)

        delete_button = Button(btn_Frame, text="DELETE",font=('arial', 12, 'bold'),bg = 'deep sky blue',width=10, bd=5,command=self.delete_info)
        delete_button.grid(row=1, column=0, padx=10, pady=10)

        clear_button = Button(btn_Frame, text="CLEAR",font=('arial', 12, 'bold'),bg = 'deep sky blue', width=10, bd=5,command=self.clear)
        clear_button.grid(row=1, column=2, padx=10, pady=10)

        show_button = Button(btn_Frame, text="SHOW", font=('arial', 12, 'bold'), bg='light blue', width=10, bd=5,
                             command=self.show_product)
        show_button.grid(row=0, column=1, padx=10, pady=10)

        Lout_button = Button(btn_Frame, text="LOGOUT", font=('arial', 12, 'bold'),bg = 'light blue', width=10, bd=5, command=self.logout)
        Lout_button.grid(row=1, column=1, padx=10, pady=10)

        #=============Detail Frame====================================

        self.RightFrame = Frame(self.root, bd=4, relief=RIDGE, bg='light blue')
        self.RightFrame.place(x=520, y=100, width=800, height=560)

        lbl_search=Label(self.RightFrame,text="Search By", font=('arial', 20, 'bold'), bg='light blue')
        lbl_search.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.search_txt= Entry(self.RightFrame,font=('arial', 13, 'bold'),bd=5,width=15, relief=GROOVE, textvariable=self.Search)
        self.search_txt.grid(row=0, column=2, padx=10, pady=10, stick='w')

        search_btn = Button(self.RightFrame, text="Search",width=10, bd=5, command=self.searchData).grid(row=0, column=3, padx=10, pady=10)
        sort_btn = Button(self.RightFrame, text="Sort", width=10, bd=5, command=self.sortData).grid(row=0, column=4, padx=10, pady=10)

        self.cboSort=ttk.Combobox(self.RightFrame,state="readonly",textvariable=self.Sort)
        self.cboSort['values']=('','Name','Manufacturer')
        self.cboSort.current(0)
        self.cboSort.grid(row=0, column=5, padx=10, pady=10)
    #=======================Table Frame=====================

        TableFrame = Frame(self.RightFrame, bd=4, relief=RIDGE, bg='light blue')
        TableFrame.place(x=10, y=70, width=760, height=470)

        scroll_x=Scrollbar(TableFrame, orient=HORIZONTAL)
        scroll_y=Scrollbar(TableFrame, orient=VERTICAL)

        self.Product_table=ttk.Treeview(TableFrame,columns=("ID","Name", "Price", "Quantity", "Manufacturer", "Contact"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Product_table.xview())
        scroll_y.config(command=self.Product_table.yview())
        self.Product_table.heading("ID",text="Product ID")
        self.Product_table.heading("Name", text="Name")
        self.Product_table.heading("Price", text="Price")
        self.Product_table.heading("Quantity", text="Quantity")
        self.Product_table.heading("Manufacturer", text="Manufacturer")
        self.Product_table.heading("Contact", text="Contact")
        self.Product_table['show']="headings"
        self.Product_table.column("ID", width=50, anchor='center')
        self.Product_table.column("Name", width=50, anchor='center')
        self.Product_table.column("Price", width=50, anchor='center')
        self.Product_table.column("Quantity", width=50, anchor='center')
        self.Product_table.column("Manufacturer", width=50, anchor='center')
        self.Product_table.column("Contact", width=50,anchor='center')
        self.Product_table.pack(fill=BOTH, expand=1)
        self.Product_table.bind('<Double-1>', self.abc)
        self.fetch_product_data()

    def fetch_product_data(self):
        query = "select * from product_info"
        rows = self.db.fetch_info(query)
        if len(rows) != 0:
            self.Product_table.delete(*self.Product_table.get_children())
            for row in rows:
                self.Product_table.insert('', END, values=row)
        self.db.fetch_info(query)

    def add_info(self):
        pid = self.txt_id.get()
        name = self.txt_name.get()
        price = self.txt_price.get()
        qnt = self.txt_quantity.get()
        manufact = self.txt_manufacture.get()
        contact = self.txt_contact.get()
        print(pid)

        P = model.product.Product_info(pid, name, price, qnt, manufact, contact)
        if pid == '' or name == '' or price == '' or qnt == '' or manufact == '' or contact == '':
            messagebox.showerror("Error", "Plz fill all the data", parent=self.root)
        else:
            qry = "INSERT INTO product_info (productid,name,price,quantity,manufacturer,contact) VALUES (%s,%s,%s,%s,%s,%s)"
            values = (P.get_productid(), P.get_name(), P.get_price(), P.get_quantity(), P.get_manufacturer(), P.get_contact())
            self.db.iud(qry, values)
            self.fetch_product_data()
            self.clear()
            messagebox.showinfo("Success", "Information added", parent=self.root)

    def clear(self):
        id=self.txt_id.delete(0,END)
        name=self.txt_name.delete(0,END)
        price=self.txt_price.delete(0,END)
        quantity=self.txt_quantity.delete(0,END)
        manufacturer=self.txt_manufacture.delete(0,END)
        contact=self.txt_contact.delete(0,END)

    def delete_info(self):
        id=self.txt_id.get()
        qry = "DELETE FROM product_info WHERE productid=%s"
        values = (id,)
        self.db.iud(qry,values)
        self.on_reset()
        self.fetch_product_data()
        self.clear()
        messagebox.showinfo("Deleted successfully", "Data deleted", parent=self.root)

    def abc(self,b):
        self.value = self.Product_table.selection()[0]
        a  = self.Product_table.item(self.value, 'values')
        self.Product_table.focus()
        self.txt_id.insert(0,a[0])
        self.txt_name.insert(0,a[1])
        self.txt_price.insert(0,a[2])
        self.txt_quantity.insert(0,a[3])
        self.txt_manufacture.insert(0,a[4])
        self.txt_contact.insert(0,a[5])

    def update_data(self):
        pid=self.txt_id.get()
        name=self.txt_name.get()
        price=self.txt_price.get()
        qnt=self.txt_quantity.get()
        manufact=self.txt_manufacture.get()
        contact=self.txt_contact.get()

        P = model.product.Product_info(name, price, qnt, manufact, contact, pid)

        qry = "UPDATE product_info SET name=%s,price=%s,quantity=%s,manufacturer=%s,contact=%s WHERE productid = %s"
        values = (P.get_productid(), P.get_name(), P.get_price(), P.get_quantity(), P.get_manufacturer(), P.get_contact())
        a = self.db.iud(qry, values)
        self.on_reset()
        self.fetch_product_data()
        self.clear()
        messagebox.showinfo("Success", "Data is Updated", parent=self.root)

    def on_reset(self):
        self.Product_table.delete(*self.Product_table.get_children())
        self.Product_table.set('')

    def show_product(self):
        str = 'select * from product_info'
        rows = self.db.fetch_info(str)
        if len(rows) != 0:
            self.Product_table.delete(*self.Product_table.get_children())
            for row in rows:
                self.Product_table.insert('', END, values=row)

    def logout(self):
        plogout = messagebox.askyesno("Confirm if you want to exit", parent=self.root)
        if plogout > 0:
            self.root.destroy()
            tk = Tk()
            Frontend.login.My_Login(tk)

    def searchData(self):
        query = "select * from product_info"
        rows = self.db.fetch_info(query)
        PSearch = self.search_txt.get()
        s = model.searchnsort.My_searching().linear_search(PSearch, rows)
        if s != False:
            self.Product_table.delete(*self.Product_table.get_children())
            self.Product_table.insert("", END, values=rows[s])


    def sortData(self):
        global index
        select_Opt = self.cboSort.get()
        if select_Opt == "Name":
            index = 1
        elif select_Opt == "Manufacturer":
            index = 4
        query = "select * from product_info"
        row = self.db.fetch_info(query)
        print(row)
        try:
            sorted_record = model.searchnsort.My_sorting().insertion_sort(row, index)
            self.Product_table.delete(*self.Product_table.get_children())
            for i in sorted_record:
                self.Product_table.insert("", END, values=i)
        except:
            messagebox.showerror("error", "error", parent=self.root)

































