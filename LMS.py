import tkinter 
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import*
from tkinter import messagebox
import mysql.connector
import datetime
import PIL
from PIL import Image,ImageTk

class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        img1 = Image.open(r"C:/Users/HP/Desktop/libary3.jpg")
        img1=img1.resize((1550,140),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=100)

        #===============================variable=======================================

        self.membr_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.surname_var=StringVar()
        self.address_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.bookname_var=StringVar()
        self.author_var=StringVar()
        self.borrow_var=StringVar()
        self.due_var=StringVar()
        self.overdue_var=StringVar()
        self.latefine_var=StringVar()

        lbltitle = Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="black",fg="gold",bd=4,relief=RIDGE,font=("times new roman",40,"bold"))
        lbltitle.place(x=0,y=100,width=1550,height=50)

        frame = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="old lace")
        frame.place(x=0,y=150,width=1530,height=380)

        #===============================DataframeLeft===================================
        DataFrameLeft = LabelFrame(frame,text="Library Membership Infrormation",bg="gray80",bd=14,relief=RIDGE,font=("times new roman",17,"bold"))
        DataFrameLeft.place(x=0,y=5,width=850,height=350)

        lblMembr = Label(DataFrameLeft,bg="gray80",text="Member Type",font=("times new roman",15,"bold"),textvariable=self.membr_var,padx=2,pady=6)
        lblMembr.grid(row=0,column=0,sticky=W)

        comMembr = ttk.Combobox(DataFrameLeft,textvariable=self.membr_var,font=("times new roman",12,"bold"),width=27,state="readonly")
        comMembr["value"]=("Student","Lecturer")
        comMembr.current(0)
        comMembr.grid(row=0,column=1)

        lblTitle = Label(DataFrameLeft,bg="gray80",text="ID No.",font=("times new roman",15,"bold"),padx=2,pady=4)
        lblTitle.grid(row=1,column=0,sticky=W)
        txtTitle = Entry(DataFrameLeft,textvariable=self.id_var,font=("arial",10),width=34)
        txtTitle.grid(row=1,column=1)

        lblFirstName = Label(DataFrameLeft,bg="gray80",text="First Name",font=("times new roman",15,"bold"),padx=2,pady=4)
        lblFirstName.grid(row=2,column=0,sticky=W)
        txtFirstName = Entry(DataFrameLeft,textvariable=self.firstname_var,font=("arial",10),width=34)
        txtFirstName.grid(row=2,column=1)

        lblSurname = Label(DataFrameLeft,bg="gray80",text="Surname",font=("times new roman",15,"bold"),padx=2,pady=4)
        lblSurname.grid(row=3,column=0,sticky=W)
        txtSurname = Entry(DataFrameLeft,textvariable=self.surname_var,font=("arial",10),width=34)
        txtSurname.grid(row=3,column=1)

        lblAddress = Label(DataFrameLeft,bg="gray80",text="Address",font=("times new roman",15,"bold"),padx=2,pady=4)
        lblAddress.grid(row=4,column=0,sticky=W)
        txtAddress = Entry(DataFrameLeft,textvariable=self.address_var,font=("arial",10),width=34)
        txtAddress.grid(row=4,column=1)

        lblPCode = Label(DataFrameLeft,bg="gray80",text="Postal Code",font=("times new roman",15,"bold"),padx=2,pady=4)
        lblPCode.grid(row=5,column=0,sticky=W)
        txtPCode = Entry(DataFrameLeft,textvariable=self.postcode_var,font=("arial",10),width=34)
        txtPCode.grid(row=5,column=1)

        lblMob_no = Label(DataFrameLeft,bg="gray80",text="Mobile No.",font=("times new roman",15,"bold"),padx=2,pady=4)
        lblMob_no.grid(row=6,column=0,sticky=W)
        txtMob_no = Entry(DataFrameLeft,textvariable=self.mobile_var,font=("arial",10),width=34)
        txtMob_no.grid(row=6,column=1)

        lblBookID = Label(DataFrameLeft,bg="gray80",text="Book ID",font=("times new roman",15,"bold"),padx=2)
        lblBookID.grid(row=0,column=3,sticky=W)
        txtBookID = Entry(DataFrameLeft,textvariable=self.bookid_var,font=("arial",10),width=34)
        txtBookID.grid(row=0,column=4)

        lblBookName = Label(DataFrameLeft,bg="gray80",text="Book Name",font=("times new roman",15,"bold"),padx=2)
        lblBookName.grid(row=1,column=3,sticky=W)
        txtBookName = Entry(DataFrameLeft,textvariable=self.bookname_var,font=("arial",10),width=34)
        txtBookName.grid(row=1,column=4)

        lblAuthor = Label(DataFrameLeft,bg="gray80",text="Author Name",font=("times new roman",15,"bold"),padx=2)
        lblAuthor.grid(row=2,column=3,sticky=W)
        txtAuthor = Entry(DataFrameLeft,textvariable=self.author_var,font=("arial",10),width=34)
        txtAuthor.grid(row=2,column=4)

        lblBorrowDate = Label(DataFrameLeft,bg="gray80",text="Borrow Date",font=("times new roman",15,"bold"),padx=2)
        lblBorrowDate.grid(row=3,column=3,sticky=W)
        txtBorrowDate = Entry(DataFrameLeft,textvariable=self.borrow_var,font=("arial",10),width=34)
        txtBorrowDate.grid(row=3,column=4)

        lblDueDate = Label(DataFrameLeft,bg="gray80",text="Due Date",font=("times new roman",15,"bold"),padx=2)
        lblDueDate.grid(row=4,column=3,sticky=W)
        txtDueDate = Entry(DataFrameLeft,textvariable=self.due_var,font=("arial",10),width=34)
        txtDueDate.grid(row=4,column=4)

        lblDays_overdue = Label(DataFrameLeft,bg="gray80",text="Days Overdue",font=("times new roman",15,"bold"),padx=2)
        lblDays_overdue.grid(row=5,column=3,sticky=W)
        txtDays_overdue = Entry(DataFrameLeft,textvariable=self.overdue_var,font=("arial",10),width=34)
        txtDays_overdue.grid(row=5,column=4)

        lblLateFine = Label(DataFrameLeft,bg="gray80",text="Late Fine",font=("times new roman",15,"bold"),padx=2)
        lblLateFine.grid(row=6,column=3,sticky=W)
        txtLateFine = Entry(DataFrameLeft,textvariable=self.latefine_var,font=("arial",10),width=34)
        txtLateFine.grid(row=6,column=4)


        #=========================Data Frame Right===============================
        DataFrameRight = LabelFrame(frame,text="Book Details",bg="gray80",bd=14,relief=RIDGE,font=("times new roman",17,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtBox = Text(DataFrameRight, font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks = ['Zombie Day','A Song of Ice & Fire','Harry Potter & The Half Blood Prince','Harry Potter & The Deathly Hallows','The Mysterious Affair at Styles',
                     'In Search of Lost Time','Murder on the Orient Express']

        def SelectBook(event=""):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if(x=="Zombie Day"):
                self.bookid_var.set("1")
                self.bookname_var.set("Zombie Day")
                self.author_var.set("Kazi Nazrul Islam")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.overdue_var.set("NO")
                self.latefine_var("50")
            elif(x=="A Song of Ice & Fire"):
                self.bookid_var.set("3")
                self.bookname_var.set("A Song of Ice & Fire")
                self.author_var.set("George R. R. Martin")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.overdue_var.set("5")
                self.latefine_var("100")
            elif(x=="Harry Potter & The Half Blood Prince"):
                self.bookid_var.set("4")
                self.bookname_var.set("Harry Potter & The Half Blood Prince")
                self.author_var.set("J.K Rowling")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.overdue_var.set("NO")
                self.latefine_var("100")
            elif(x=="Harry Potter & The Deathly Hallows"):
                self.bookid_var.set("5")
                self.bookname_var.set("Harry Potter & The Deathly Hallows")
                self.author_var.set("J.K Rowling")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.overdue_var.set("7")
                self.latefine_var("100")
            elif(x=="The Mysterious Affair at Styles"):
                self.bookid_var.set("7")
                self.bookname_var.set("The Mysterious Affair at Styles")
                self.author_var.set("Agatha Christie")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.overdue_var.set("3")
                self.latefine_var("50")
            elif(x=="In Search of Lost Time"):
                self.bookid_var.set("10")
                self.bookname_var.set("In Search of Lost Time")
                self.author_var.set("Marcel Proust")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.overdue_var.set("3")
                self.latefine_var("50")
            elif(x=="Murder on the Orient Express"):
                self.bookid_var.set("2")
                self.bookname_var.set("Murder on the Orient Express")
                self.author_var.set("Agatha Christie")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.borrow_var.set(d1)
                self.due_var.set(d3)
                self.overdue_var.set("7")
                self.latefine_var("100")

            
        listBox = Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

        #========================Buttons Frame==========================
        Framebutton = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="snow")
        Framebutton.place(x=0,y=530,width=1530,height=60)

        btnAddData = Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="dark green",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData = Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=23,bg="indian red",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData = Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=23,bg="dark green",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData = Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg="indian red",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData = Button(Framebutton,command = self.reset,text="Reset Data",font=("arial",12,"bold"),width=23,bg="dark green",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData = Button(Framebutton,command = self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="indian red",fg="white")
        btnAddData.grid(row=0,column=5)


        #========================Information Frame==========================
        FrameDetails = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="old lace")
        FrameDetails.place(x=0,y=590,width=1530,height=210)

        Table_frame = Frame(FrameDetails,bd=6,relief=RIDGE,bg="gray80")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("MemberType","IDno","Firstname","Surname","Address","Postalcode","Mobileno.",
                                                             "Bookid","Bookname","Author","Borrowdate","Duedate","Daysoverdue","Latefine"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fil=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("MemberType",text="Member Type")
        self.library_table.heading("IDno",text="ID No.")
        self.library_table.heading("Firstname",text="First Name")
        self.library_table.heading("Surname",text="Surname")
        self.library_table.heading("Address",text="Address")
        self.library_table.heading("Postalcode",text="Post Code")
        self.library_table.heading("Mobileno.",text="Mob No.")
        self.library_table.heading("Bookid",text="Book ID")
        self.library_table.heading("Bookname",text="Book Name")
        self.library_table.heading("Author",text="Author")
        self.library_table.heading("Borrowdate",text="Borrow Date")
        self.library_table.heading("Duedate",text="Due Date")
        self.library_table.heading("Daysoverdue",text="Date Overdue")
        self.library_table.heading("Latefine",text="Late Fine")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("MemberType",width=150)
        self.library_table.column("IDno",width=150)
        self.library_table.column("Firstname",width=150)
        self.library_table.column("Surname",width=150)
        self.library_table.column("Address",width=150)
        self.library_table.column("Postalcode",width=150)
        self.library_table.column("Mobileno.",width=150)
        self.library_table.column("Bookid",width=150)
        self.library_table.column("Bookname",width=150)
        self.library_table.column("Author",width=150)
        self.library_table.column("Borrowdate",width=150)
        self.library_table.column("Duedate",width=150)
        self.library_table.column("Daysoverdue",width=150)
        self.library_table.column("Latefine",width=150)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Mbiswas@2004",database="madhurima")
        curr = conn.cursor()
        curr.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                  self.membr_var.get(),
                                                                                  self.id_var.get(),
                                                                                  self.firstname_var.get(),
                                                                                  self.surname_var.get(),
                                                                                  self.address_var.get(),
                                                                                  self.postcode_var.get(),
                                                                                  self.mobile_var.get(),
                                                                                  self.bookid_var.get(),
                                                                                  self.bookname_var.get(),
                                                                                  self.author_var.get(),
                                                                                  self.borrow_var.get(),
                                                                                  self.due_var.get(),
                                                                                  self.overdue_var.get(),
                                                                                  self.latefine_var.get()
                                                                                  ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Member has been added successfully")

    def update(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Mbiswas@2004",database="madhurima")
        curr = conn.cursor()
        curr.execute("update library set MemberType=%s,Firstname=%s,Surname=%s,Address=%s,Postalcode=%s,`Mobileno.`=%s,Bookid=%s,Bookname=%s,Author=%s,Borrowdate=%s,Duedate=%s,Daysoverdue=%s,Latefine=%s where IDno=%s",(
        
                                                                                  self.membr_var.get(),

                                                                                  self.firstname_var.get(),
                                                                                  self.surname_var.get(),
                                                                                  self.address_var.get(),
                                                                                  self.postcode_var.get(),
                                                                                  self.mobile_var.get(),
                                                                                  self.bookid_var.get(),
                                                                                  self.bookname_var.get(),
                                                                                  self.author_var.get(),
                                                                                  self.borrow_var.get(),
                                                                                  self.due_var.get(),
                                                                                  self.overdue_var.get(),
                                                                                  self.latefine_var.get(),
                                                                                  self.id_var.get()
                                                                                  ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Successful","Member has been updated")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Mbiswas@2004",database="madhurima")
        curr = conn.cursor()
        curr.execute("select * from library")
        rows = curr.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content["values"]

        self.membr_var.set(row[0]),
        self.id_var.set(row[1]),
        self.firstname_var.set(row[2]),
        self.surname_var.set(row[3]),
        self.address_var.set(row[4]),
        self.postcode_var.set(row[5]),
        self.mobile_var.set(row[6]),
        self.bookid_var.set(row[7]),
        self.bookname_var.set(row[8]),
        self.author_var.set(row[9]),
        self.borrow_var.set(row[10]),
        self.due_var.set(row[11]),
        self.overdue_var.set(row[12]),
        self.latefine_var.set(row[13])

    def showData(self):
        self.txtBox.insert(END,("Member Type\t\t"+self.membr_var.get()+"\n"))
        self.txtBox.insert(END,("ID No.\t\t"+self.id_var.get()+"\n"))
        self.txtBox.insert(END,("First Name\t\t"+self.firstname_var.get()+"\n"))
        self.txtBox.insert(END,("Surname\t\t"+self.surname_var.get()+"\n"))
        self.txtBox.insert(END,("Address\t\t"+self.address_var.get()+"\n"))
        self.txtBox.insert(END,("Postal Code\t\t"+self.postcode_var.get()+"\n"))
        self.txtBox.insert(END,("Mobile No.\t\t"+self.mobile_var.get()+"\n"))
        self.txtBox.insert(END,("Book ID\t\t"+self.bookid_var.get()+"\n"))
        self.txtBox.insert(END,("Book Name\t\t"+self.bookname_var.get()+"\n"))
        self.txtBox.insert(END,("Author\t\t"+self.author_var.get()+"\n"))
        self.txtBox.insert(END,("Borrow Date\t\t"+self.borrow_var.get()+"\n"))
        self.txtBox.insert(END,("Due Date\t\t"+self.due_var.get()+"\n"))
        self.txtBox.insert(END,("Days Overdue\t\t"+self.overdue_var.get()+"\n"))
        self.txtBox.insert(END,("Late Fine\t\t"+self.latefine_var.get()+"\n"))

    def reset(self):
        self.membr_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.surname_var.set(""),
        self.address_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.bookname_var.set(""),
        self.author_var.set(""),
        self.borrow_var.set(""),
        self.due_var.set(""),
        self.overdue_var.set(""),
        self.latefine_var.set("")
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Library Management System","Do you want to exit?")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.id_var.get=="":
            messagebox.showerror("Error","Select the member")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="Mbiswas@2004",database="madhurima")
            curr = conn.cursor()
            query = "delete from library where IDno=%s"
            value = (self.id_var.get(),)
            curr.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been deleted")
        

if __name__ == "__main__":
    root = Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
