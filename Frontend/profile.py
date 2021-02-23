from tkinter import *
from tkinter import ttk

class Warehouse:
    def __init__(self, root):
        self.root = root
        self.root.config(bg='grey')
        self.root.title('Inventory WareHouse Records')
        self.root.geometry('1350x700')

        ititle=Label(self.root,text='WAREHOUSE INVENTORY MANAGEMENT SYSTEM',bd=5, relief=GROOVE,\
                    font=('arial', 35, 'bold'), bg="deep sky blue")
        ititle.pack(side=TOP, fill=X)

    #================ Manage Frame===============================

        LeftFrame=Frame(self.root, bd=4, relief=RIDGE, bg='lavender')
        LeftFrame.place(x=30, y=100, width=450, height=560)

        Lefttitle=Label(LeftFrame, text="Product Information", font=('arial', 20, 'bold'), bg='lavender')
        Lefttitle.grid(row=0, columnspan=2, pady=20)

        lbl_id=Label(LeftFrame, text="Product ID", font=('arial', 15, 'bold'), bg='lavender')
        lbl_id.grid(row=1, column=0, pady=10, padx=10, sticky='w')

        txt_id=Entry(LeftFrame, font=('arial', 15, 'bold'),relief=GROOVE, bd=5)
        txt_id.grid(row=1, column=1, pady=10, padx=10, sticky='w')

        lbl_name = Label(LeftFrame, text="Product Name", font=('arial', 15, 'bold'), bg='lavender')
        lbl_name.grid(row=2, column=0, pady=10, padx=10, sticky='w')

        txt_name = Entry(LeftFrame, font=('arial', 15, 'bold'), relief=GROOVE, bd=5)
        txt_name.grid(row=2, column=1, pady=10, padx=10, sticky='w')

        lbl_price = Label(LeftFrame, text="Product Price", font=('arial', 15, 'bold'), bg='lavender')
        lbl_price.grid(row=3, column=0, pady=10, padx=10, sticky='w')

        txt_price = Entry(LeftFrame, font=('arial', 15, 'bold'), relief=GROOVE, bd=5)
        txt_price.grid(row=3, column=1, pady=10, padx=10, sticky='w')

        lbl_quantity = Label(LeftFrame, text="Product Quantity", font=('arial', 15, 'bold'), bg='lavender')
        lbl_quantity.grid(row=4, column=0, pady=10, padx=10, sticky='w')

        txt_quantity = Entry(LeftFrame, font=('arial', 15, 'bold'), relief=GROOVE, bd=5)
        txt_quantity.grid(row=4, column=1, pady=10, padx=10, sticky='w')

        lbl_manufacture = Label(LeftFrame, text="Manufacturer", font=('arial', 15, 'bold'), bg='lavender')
        lbl_manufacture.grid(row=5, column=0, pady=10, padx=10, sticky='w')

        txt_manufacture = Entry(LeftFrame, font=('arial', 15, 'bold'), relief=GROOVE, bd=5)
        txt_manufacture.grid(row=5, column=1, pady=10, padx=10, sticky='w')

        lbl_contact = Label(LeftFrame, text="Company Contact", font=('arial', 15, 'bold'), bg='lavender')
        lbl_contact.grid(row=6, column=0, pady=10, padx=10, sticky='w')

        txt_contact = Entry(LeftFrame, font=('arial', 15, 'bold'), relief=GROOVE, bd=5)
        txt_contact.grid(row=6, column=1, pady=10, padx=10, sticky='w')

    #====================Button Frame=====================
        btn_Frame=Frame(LeftFrame, bd=4, bg='lavender', relief=RIDGE)
        btn_Frame.place(x=40, y=420, width=350)

        add_button=Button(btn_Frame, text="ADD", font=('arial', 12, 'bold'),width=10, bd=5)
        add_button.grid(row=0, column=0, padx=10, pady=10)

        update_button = Button(btn_Frame, text="UPDATE",font=('arial', 12, 'bold'), width=10, bd=5)
        update_button.grid(row=0, column=1, padx=10, pady=10)

        delete_button = Button(btn_Frame, text="DELETE",font=('arial', 12, 'bold'), width=10, bd=5)
        delete_button.grid(row=1, column=0, padx=10, pady=10)

        clear_button = Button(btn_Frame, text="CLEAR",font=('arial', 12, 'bold'), width=10, bd=5)
        clear_button.grid(row=1, column=1, padx=10, pady=10)

        #=============Detail Frame====================================

        RightFrame = Frame(self.root, bd=4, relief=RIDGE, bg='light blue')
        RightFrame.place(x=520, y=100, width=800, height=560)

        lbl_search=Label(RightFrame,text="Search By", font=('arial', 20, 'bold'), bg='light blue')
        lbl_search.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        combo_search=ttk.Combobox(RightFrame,font=('Italic', 13, 'bold'), state='read only')
        combo_search['values']=("ID","Name")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        search_txt= Entry(RightFrame,font=('arial', 13, 'bold'),bd=5,width=15, relief=GROOVE)
        search_txt.grid(row=0, column=2, padx=10, pady=10, stick='w')

        search_btn = Button(RightFrame, text="Search",width=10, bd=5).grid(row=0, column=3, padx=10, pady=10)
        showall_btn = Button(RightFrame, text="Show All", width=10, bd=5).grid(row=0, column=4, padx=10, pady=10)

    #=======================Table Frame=====================

        TableFrame = Frame(RightFrame, bd=4, relief=RIDGE, bg='light blue')
        TableFrame.place(x=10, y=70, width=760, height=470)

        scroll_x=Scrollbar(TableFrame, orient=HORIZONTAL)
        scroll_y=Scrollbar(TableFrame, orient=VERTICAL)

        Product_table=ttk.Treeview(TableFrame,columns=("ID","Name", "Price", "Quantity", "Manufacturer", "Contact"),\
                                   xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Product_table.xview())
        scroll_y.config(command=Product_table.yview())
        Product_table.heading("ID",text="Product ID")
        Product_table.heading("Name", text="Name")
        Product_table.heading("Price", text="Price")
        Product_table.heading("Quantity", text="Quantity")
        Product_table.heading("Manufacturer", text="Manufacturer")
        Product_table.heading("Contact", text="Contact")
        Product_table['show']="headings"
        Product_table.column("ID", width=50)
        Product_table.column("Name", width=50)
        Product_table.column("Price", width=50)
        Product_table.column("Quantity", width=50)
        Product_table.column("Manufacturer", width=50)
        Product_table.column("Contact", width=50)
        Product_table.pack(fill=BOTH, expand=1)



























