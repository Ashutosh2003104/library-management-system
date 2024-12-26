from tkinter import *
from tkinter import ttk
import mysql.connector

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1500x800+0+0")  

        lbtitle = Label(self.root, text="Library Management System", bg="powder blue",
                        fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbtitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd =12, relief = RIDGE, padx = 20 , bg ="powder blue")
        frame.place(x=0, y=130, width = 1530,height = 400)

        # ================ DataFrame Label =================

        DataFrameLeft=LabelFrame(frame, text = "Library Membership Information",bg="powder blue",
                        fg="green", bd=12, relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width = 900, height=350)
 
        lblMember = Label(DataFrameLeft, bg = "powder blue" ,text ="Member Type", font = ("times new roman", 15, "bold"), padx = 2, pady=6)
        lblMember.grid(row = 0, column = 0, sticky = W)

        comMember = ttk.Combobox(DataFrameLeft,font = ("times new roman", 15, "bold"),width = 27,state = "readonly")
        comMember["values"] = ("Admin Staf","Student","Lecturer")
        comMember.grid(row = 0,column = 1)

        lblPRN_No = Label(DataFrameLeft, bg = "powder blue" ,text ="PRN number", font = ("times new roman", 15, "bold"), padx = 2, pady=6)
        lblPRN_No.grid(row = 1, column = 0, sticky = W)

        txtPRN_NO = Entry(DataFrameLeft,font = ("times new roman", 15, "bold"), width = 29)
        txtPRN_NO.grid(row = 1, column = 1)

        lblTitle = Label(DataFrameLeft, bg = "powder blue" ,text ="Id No", font = ("arial", 12, "bold"), padx = 2, pady=4)
        lblTitle.grid(row = 1, column = 0, sticky = W)
        txtTitle = Entry(DataFrameLeft, font = ("arial",13,"bold"),width = 29)
        txtTitle.grid(row = 2, column = 1)

        lblFirstName = Label(DataFrameLeft, bg = "powder blue" ,text ="First Name", font = ("arial", 12, "bold"), padx = 2, pady=4)
        lblFirstName.grid(row = 3, column = 0, sticky = W)
        txtFirstName = Entry(DataFrameLeft, font = ("arial",13,"bold"),width = 29)
        txtFirstName.grid(row = 3, column = 1)

        lblLastName = Label(DataFrameLeft, bg="powder blue", text="Last Name", font=("arial", 12, "bold"), padx=2, pady=4)
        lblLastName.grid(row=1, column=2, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtLastName.grid(row=1, column=3)

        lblAddress1 = Label(DataFrameLeft, bg="powder blue", text="Address 1", font=("arial", 12, "bold"), padx=2, pady=4)
        lblAddress1.grid(row=2, column=2, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtAddress1.grid(row=2, column=3)

        lblAddress2 = Label(DataFrameLeft, bg="powder blue", text="Address 2", font=("arial", 12, "bold"), padx=2, pady=4)
        lblAddress2.grid(row=3, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtAddress2.grid(row=3, column=1)

        lblPostCode = Label(DataFrameLeft, bg="powder blue", text="Post Code", font=("arial", 12, "bold"), padx=2, pady=4)
        lblPostCode.grid(row=3, column=2, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtPostCode.grid(row=3, column=3)

        lblMobile = Label(DataFrameLeft, bg="powder blue", text="Mobile", font=("arial", 12, "bold"), padx=2, pady=4)
        lblMobile.grid(row=4, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtMobile.grid(row=4, column=1)

        lblBookId = Label(DataFrameLeft, bg="powder blue", text="Book ID", font=("arial", 12, "bold"), padx=2, pady=4)
        lblBookId.grid(row=4, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtBookId.grid(row=4, column=3)

        lblBookTitle = Label(DataFrameLeft, bg="powder blue", text="Book Title", font=("arial", 12, "bold"), padx=2, pady=4)
        lblBookTitle.grid(row=5, column=0, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtBookTitle.grid(row=5, column=1)

        lblAuthor = Label(DataFrameLeft, bg="powder blue", text="Author", font=("arial", 12, "bold"), padx=2, pady=4)
        lblAuthor.grid(row=5, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtAuthor.grid(row=5, column=3)

        lblDateBorrowed = Label(DataFrameLeft, bg="powder blue", text="Date Borrowed", font=("arial", 12, "bold"), padx=2, pady=4)
        lblDateBorrowed.grid(row=6, column=0, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtDateBorrowed.grid(row=6, column=1)

        lblDateDue = Label(DataFrameLeft, bg="powder blue", text="Date Due", font=("arial", 12, "bold"), padx=2, pady=4)
        lblDateDue.grid(row=6, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtDateDue.grid(row=6, column=3)

        lblDaysOnBook = Label(DataFrameLeft, bg="powder blue", text="Days on Book", font=("arial", 12, "bold"), padx=2, pady=4)
        lblDaysOnBook.grid(row=7, column=0, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtDaysOnBook.grid(row=7, column=1)

        lblLateReturnFine = Label(DataFrameLeft, bg="powder blue", text="Late Return Fine", font=("arial", 12, "bold"), padx=2, pady=4)
        lblLateReturnFine.grid(row=7, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtLateReturnFine.grid(row=7, column=3)

        lblDateOverDue = Label(DataFrameLeft, bg="powder blue", text="Date Over Due", font=("arial", 12, "bold"), padx=2, pady=4)
        lblDateOverDue.grid(row=8, column=0, sticky=W)
        txtDateOverDue = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtDateOverDue.grid(row=8, column=1)

        lblActualPrice = Label(DataFrameLeft, bg="powder blue", text="Actual Price", font=("arial", 12, "bold"), padx=2, pady=4)
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtActualPrice.grid(row = 8, column = 3)





# ================== DataFrame Right =================================
       # ================== DataFrame Right =================================
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue",
                                    fg="green", bd=12, relief=RIDGE, font=("arial", 12, "bold"))
        DataFrameRight.place(x=870, y=5, width=580, height=350)

        self.txtBox = Text(DataFrameRight, font=("arial", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar = Scrollbar(DataFrameRight, width=32)  # Remove unnecessary padx and pady
        listScrollbar.grid(row=0, column=1, sticky="ns")

        listBooks = [
    "The Catcher in the Rye",
    "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Great Gatsby",
    "Moby Dick",
    "The Hobbit",
    "War and Peace",
    "Crime and Punishment",
    "The Adventures of Huckleberry Finn",
    "Brave New World",
    "Wuthering Heights",
    "The Lord of the Rings",
    "Anna Karenina",
    "Jane Eyre",
    "Fahrenheit 451",
    "The Brothers Karamazov",
    "The Alchemist",
    "Les Misérables",
    "The Picture of Dorian Gray",
    "A Tale of Two Cities",
    "Frankenstein",
    "Dracula",
    "Don Quixote",
    "The Scarlet Letter",
    "Great Expectations",
    "Emma",
    "The Old Man and the Sea",
    "Of Mice and Men",
    "Slaughterhouse-Five"
]

        listBox = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=20, height=16)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)

        # ================= Button Frame ======================
        Framebutton = Frame(self.root, bd =12, relief = RIDGE, padx = 20 , bg ="powder blue")
        Framebutton.place(x=0, y=530, width = 1530,height = 70)

        btnAddData = Button(Framebutton, text = "Add Data", font = ("arial", 12, "bold"), width = 23, bg = "blue", fg = "white")
        btnAddData.grid(row = 0, column = 0)

        btnAddData = Button(Framebutton, text = "Show Data", font = ("arial", 12, "bold"), width = 23, bg = "blue", fg = "white")
        btnAddData.grid(row = 0, column = 1)

        btnAddData = Button(Framebutton, text = "Update", font = ("arial", 12, "bold"), width = 23, bg = "blue", fg = "white")
        btnAddData.grid(row = 0, column = 2)

        btnAddData = Button(Framebutton, text = "Delete", font = ("arial", 12, "bold"), width = 23, bg = "blue", fg = "white")
        btnAddData.grid(row = 0, column = 3)

        btnAddData = Button(Framebutton, text = "Reset", font = ("arial", 12, "bold"), width = 23, bg = "blue", fg = "white")
        btnAddData.grid(row = 0, column = 4)

        btnAddData = Button(Framebutton, text = "Exit", font = ("arial", 12, "bold"), width = 23, bg = "blue", fg = "white")
        btnAddData.grid(row = 0, column = 5)

        FrameDetails = Frame(self.root, bd =12, relief = RIDGE, padx = 20 , bg ="powder blue")
        FrameDetails.place(x=0, y=600, width = 1530,height = 190)


        Table_frame = Frame(FrameDetails, bd = 6, relief = RIDGE, bg = "powder blue")
        Table_frame.place(x=0, y=2, width = 1460, height = 190)

        xscroll = ttk.Scrollbar(Table_frame, orient = HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient = VERTICAL)


        self.library_table = ttk.Treeview(Table_frame, column = ("membertype","prnno", "idno", "firstname", "lastname", 
        "address1", "address2", "postcode", "mobile", 
        "bookid", "booktitle", "author", 
        "dateborrowed", "datedue", "daysonbook", 
        "latereturnfine", "dateoverdue", "finalprice") ,xscrollcommand = xscroll.set,yscrollcommand = yscroll.set)

        xscroll.pack(side = BOTTOM,  fill = X)
        yscroll.pack(side = RIGHT, fill = Y )

        xscroll.config(command = self.library_table.xview)
        yscroll.config(command = self.library_table.yview)


        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN Number")
        self.library_table.heading("idno", text="ID Number")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address 1")
        self.library_table.heading("address2", text="Address 2")
        self.library_table.heading("postcode", text="Post Code")
        self.library_table.heading("mobile", text="Mobile")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("daysonbook", text="Days on Book")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Over Due")
        self.library_table.heading("finalprice", text="Actual Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill = BOTH, expand = 1)

        self.library_table.column("membertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("idno", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postcode", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=150)
        self.library_table.column("author", width=150)
        self.library_table.column("dateborrowed", width=120)
        self.library_table.column("datedue", width=120)
        self.library_table.column("daysonbook", width=120)
        self.library_table.column("latereturnfine", width=120)
        self.library_table.column("dateoverdue", width=120)
        self.library_table.column("finalprice", width=100)



if __name__ == "__main__":  # Corrected condition
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
