import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox
import datetime

def welcome():
    global root
    root=Tk()
    root.title("Library Managemnet System")
    root.geometry("400x200+400+200")
    root.resizable(FALSE,FALSE)
    l1=Label(root, text="Welcome to the Library Management System !!",font=('times',
             16),fg='dark blue').pack()
    l2=Label(root,text='Please choose a login format.',font=('helvetica',12))
    l2.place(x=20,y=35)
    b1=Button(root,text='LOGIN AS LIBRARIAN',command=welcomelibr).place(x=20,y=90)
    b2=Button(root,text='LOGIN AS STUDENT',command=welcomestu).place(x=200,y=90)
    root.mainloop()

def welcomelibr():
    def back():
        root1.destroy()
        welcome()
    global root1
    root1 = Tk()
    root1.title("Library Managemnet System")
    root1.geometry("400x200+400+200")
    root1.resizable(FALSE, FALSE)
    l1 = Label(root1, text="LOGIN AS LIBRARIAN", font=('times',16), fg='dark blue').pack()
    usr = Label(root1,text='Librarian Id:').place(x=20, y=35)
    pwd=Label(root1,text='Password:').place(x=20,y=65)
    usernamelibr=StringVar()
    passwordlibr=StringVar()
    entryusr=Entry(root1,textvariable=usernamelibr).place(x=90,y=35)
    entrypwd=Entry(root1,show='*',textvariable=passwordlibr).place(x=90,y=65)
    loginbutton=ttk.Button(root1, text='LOGIN',command=loginlibr).place(x=90,y=100)
    destroybutton = ttk.Button(root1, text='Back', command=back).place(x=200, y=100)
    try:
        root.destroy()
    except:
        pass

def welcomestu():
    def back():
        root2.destroy()
        welcome()
    global root2
    root2 = Tk()
    root2.title("Library Managemnet System")
    root2.geometry("400x200+400+200")
    root2.resizable(FALSE, FALSE)
    l1 = Label(root2, text="LOGIN AS STUDENT", font=('times', 16), fg='dark blue').pack()
    usr = Label(root2, text='Student Id:').place(x=20, y=35)
    pwd = Label(root2, text='Password:').place(x=20, y=65)
    usernamestu=StringVar()
    passwordstu=StringVar()
    entryusr = Entry(root2,textvariable=usernamestu).place(x=90, y=35)
    entrypwd = Entry(root2,show='*',textvariable=passwordstu).place(x=90, y=65)
    loginbutton = ttk.Button(root2, text='LOGIN',command=loginstu).place(x=90, y=100)
    destroybutton=ttk.Button(root2, text='Back',command=back).place(x=200,y=100)
    try:
        root.destroy()
    except:
        pass
def error():
    messagebox.showinfo('No updates!', 'This feature is yet to be launched')
def loginlibr():
    global loginwin
    try:
        root1.destroy()
    except:
        pass
    def logout():
        loginwin.destroy()
        welcomelibr()
    loginwin = Tk()
    loginwin.title("Librarian Window")
    loginwin.geometry('400x300+400+150')
    loginwin.resizable(FALSE, FALSE)
    ttk.Button(loginwin, text="Add Book", command=addbook, width=20).place(x=130, y=20)
    ttk.Button(loginwin, text="Remove Book", width=20,command=error).place(x=130, y=60)
    ttk.Button(loginwin, text="View Book", width=20,command=viewbooks).place(x=130, y=100)
    ttk.Button(loginwin, text="Issue Book", command=issuebook, width=20).place(x=130, y=140)
    ttk.Button(loginwin, text="Logout", width=20, command=logout).place(x=130, y=180)
    loginwin.mainloop()
    try:
        root1.destroy()
    except:
        pass
def nextwindowinlibr():
    try:
        loginwin.destroy()
    except:
        pass


def addbook():
    def back():
        addwin.destroy()
        loginlibr()
    nextwindowinlibr()
    global addwin,addbookname,addauthor,addquantity,addbookno
    addwin=Tk()
    addwin.title("ADD BOOK")
    addwin.geometry('400x250+400+200')
    addwin.resizable(FALSE,FALSE)
    Label(addwin,text='Add Book',font=('times',20)).pack()
    ttk.Label(addwin,text="Book Name:").place(x=20,y=50)
    ttk.Label(addwin, text="Author Name:").place(x=20, y=80)
    ttk.Label(addwin, text="Quantity:").place(x=20, y=110)
    ttk.Label(addwin, text="Book No:").place(x=20, y=140)
    addbookname=StringVar()
    addauthor = StringVar()
    addquantity= StringVar()
    addbookno = StringVar()
    nameentry=ttk.Entry(addwin,textvariable=addbookname).place(x=100,y=50)
    authorentry=ttk.Entry(addwin,textvariable=addauthor).place(x=100,y=80)
    quantityentry=ttk.Entry(addwin,textvariable=addquantity).place(x=100,y=110)
    booknoentry=ttk.Entry(addwin,textvariable=addbookno).place(x=100,y=140)
    ttk.Button(addwin,text='Add',command=addbookbutton).place(x=200,y=170)
    ttk.Button(addwin,text='Close',command=back).place(x=200,y=200)
    addwin.mainloop()

def addbookbutton():
    global bookname, author, quantity,bookno
    bookname = addbookname.get()
    author=addauthor.get()
    quantity=addquantity.get()
    bookno=addbookno.get()
    userfile = open('Books', 'w')
    bookappend = userfile.write(bookname + '\n')
    authorappend = userfile.write(author + '\n')
    quantityappend = userfile.write(quantity + '\n')
    booknoappend = userfile.write(bookno + '\n')
    userfile.close()
    messagebox.showinfo('Book Added', 'The book has been successfully added.')
    addwin.destroy()
    loginlibr()

def viewbooks():
    viewwin = Tk()
    loginwin.destroy()
    def back():
        viewwin.destroy()
        loginlibr()

    a=open('Books','r')
    viewbookname = (a.readline())
    viewauthor = (a.readline())
    viewquantity = (a.readline())
    viewbookno = (a.readline())
    yaxis = 60
    viewwin.geometry('500x350+400+150')
    viewwin.title("View Books")
    viewwin.resizable(FALSE, FALSE)
    Label(viewwin, text='Book Name', font=('times', 12)).place(x=10, y=30)
    Label(viewwin, text='Author', font=('times', 12)).place(x=180, y=30)
    Label(viewwin, text='Quantity', font=('times', 12)).place(x=290, y=30)
    Label(viewwin, text='Book No', font=('times', 12)).place(x=360, y=30)
    ttk.Button(viewwin, text='Back', command=back).place(x=400, y=300)
    Label(viewwin, text=viewbookname, font=('times', 10)).place(x=10, y=yaxis)
    Label(viewwin, text=viewauthor, font=('times', 10)).place(x=180, y=yaxis)
    Label(viewwin, text=viewquantity, font=('times', 10)).place(x=310, y=yaxis)
    Label(viewwin, text=viewbookno, font=('times', 10)).place(x=375, y=yaxis)
    yaxis+=20


    viewwin.mainloop()


months=['January','February','March','April','May','June','July','August','September','October','November','December']
years=list(range(2021,2031))
days=list(range(1,32))
def issuebook():
    def back():
        issuewin.destroy()
        loginlibr()
    nextwindowinlibr()
    global issuewin
    issuewin = Tk()
    issuewin.title("Issue Book")
    issuewin.geometry('400x250+400+200')
    issuewin.resizable(FALSE, FALSE)
    Label(issuewin,text='Issue Book',font=("times",20)).pack()
    ttk.Label(issuewin, text="User ID:").place(x=20, y=30)
    ttk.Label(issuewin, text="Book No:").place(x=20, y=60)
    ttk.Label(issuewin, text="Issue Date:").place(x=20, y=90)
    ttk.Label(issuewin, text="Expiry Date:").place(x=20, y=120)
    ttk.Button(issuewin, text="Issue",command=error).place(x=20, y=150)
    ttk.Button(issuewin, text="Close",command=back).place(x=20, y=180)
    y1=Combobox(issuewin,values=days,width=3).place(x=80,y=90)
    m1=Combobox(issuewin, values=months,width=10).place(x=120, y=90)
    d1=Combobox(issuewin, values=years,width=4).place(x=200, y=90)
    y2 = Combobox(issuewin, values=days, width=3).place(x=90, y=120)
    m2 = Combobox(issuewin, values=months, width=10).place(x=130,y=120)
    d2 = Combobox(issuewin, values=years, width=4).place(x=210, y=120)
    issueuser=ttk.Entry(issuewin).place(x=80,y=30)
    issuebookno=ttk.Entry(issuewin).place(x=80,y=60)
    issuewin.mainloop()

def loginstu():
    try:
        root2.destroy()
    except:
        pass

    def viewbooks():
        viewwin = Tk()
        loginwin1.destroy()

        def back():
            viewwin.destroy()
            loginstu()

        a = open('Books', 'r')
        viewbookname = (a.readline())
        viewauthor = (a.readline())
        viewquantity = (a.readline())
        viewbookno = (a.readline())
        yaxis = 60
        viewwin.geometry('500x350+400+150')
        viewwin.title("Available Books")
        viewwin.resizable(FALSE, FALSE)
        Label(viewwin, text='Book Name', font=('times', 12)).place(x=10, y=30)
        Label(viewwin, text='Author', font=('times', 12)).place(x=180, y=30)
        Label(viewwin, text='Quantity', font=('times', 12)).place(x=290, y=30)
        Label(viewwin, text='Book No', font=('times', 12)).place(x=360, y=30)
        ttk.Button(viewwin, text='Back', command=back).place(x=400, y=300)
        Label(viewwin, text=viewbookname, font=('times', 10)).place(x=10, y=yaxis)
        Label(viewwin, text=viewauthor, font=('times', 10)).place(x=180, y=yaxis)
        Label(viewwin, text=viewquantity, font=('times', 10)).place(x=310, y=yaxis)
        Label(viewwin, text=viewbookno, font=('times', 10)).place(x=375, y=yaxis)

        viewwin.mainloop()

    def logout():
        loginwin1.destroy()
        welcomestu()
    def issuebooks():
        messagebox.showinfo("Permission Denied !!",'Please ask Librarian to issue the book/s you want.')

    loginwin1 = Tk()
    loginwin1.title("Student Window")
    loginwin1.geometry('400x200+400+150')
    loginwin1.resizable(FALSE, FALSE)
    ttk.Button(loginwin1, text="Available Books",command=viewbooks, width=20).place(x=130, y=20)
    ttk.Button(loginwin1, text="Issue Books",command=issuebooks, width=20).place(x=130, y=60)
    ttk.Button(loginwin1, text="LogOut", width=20, command=logout).place(x=130, y=100)

    loginwin1.mainloop()

welcome()