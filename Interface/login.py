#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3


"""functions"""


def index():
    loginWindow.destroy()
    import admin


def clear():
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)


def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Enter Password and username')
        clear()
    else:
        try:
            connection = sqlite3.connect('database/FreeFlow.db')
            cursor = connection.cursor()
        except:
            messagebox.showerror('Error', 'Database connection Error')
            return

        query = 'SELECT * FROM userdata WHERE username = ? AND password = ?'
        cursor.execute(query, (usernameEntry.get(), passwordEntry.get()))

        row = cursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Incorrect credentials')
        else:
            messagebox.showinfo('Success', 'Login Successful')
            index()
        clear()

def forgot(event):
    messagebox.showinfo('Information', 'Contact management')
def on_username(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)


def on_password(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)


def hide():
    openeye.config(file='images/closeeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='images/openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


"""oparations"""
loginWindow = Tk()
loginWindow.geometry('1280x720+10+10')
loginWindow.resizable(0, 0)
loginWindow.title('Login Page')

bgimage = PhotoImage(file='images/bg.png')
loginbg = PhotoImage(file='images/loginbg.png')
closeeye = PhotoImage(file='images/closeeye.png')
openeye = PhotoImage(file='images/openeye.png')
icon = PhotoImage(file='images/myicon.png')

bglabel = Label(loginWindow, image=bgimage)
bglabel.place(x=0, y=0)

loginlabel = Label(loginWindow, image=loginbg, bd=0)
loginlabel.place(x=520, y=180)

heading = Label(loginWindow, text='User Login', font=('Microsoft Yahei UI Light', 15, 'bold'),
                bg='NavajoWhite3', fg='brown4')
heading.place(x=610, y=185)

usernameEntry = Entry(loginWindow, width=24, font=('Microsoft Yahei UI Light', 13, 'bold'),
                      bd=0, fg='black')
usernameEntry.place(x=540, y=275)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', on_username)

frame1 = Frame(loginWindow, width=243, height=4, bg='brown1')
frame1.place(x=540, y=300)

passwordEntry = Entry(loginWindow, width=24, font=('Microsoft Yahei UI Light', 13, 'bold'),
                      bd=0, fg='black')
passwordEntry.place(x=540, y=355)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', on_password)

frame2 = Frame(loginWindow, width=243, height=4, bg='brown1')
frame2.place(x=540, y=380)


eyeButton = Button(loginWindow, image=openeye, bd=0, cursor='hand2',
                   width=15, height=15, activebackground='white', command=hide)
eyeButton.place(x=760, y=360)

forgotButton = Button(loginWindow, text='Forgot Password?', bd=0, cursor='hand2',
                        activebackground='NavajoWhite3', activeforeground='brown1',
                        bg='NavajoWhite3', font=('Arial Sans', 8, 'bold'), command = forgot)
forgotButton.place(x=680, y=390)

loginButton = Button(loginWindow, text='Login', font=('Arial Sans', 8, 'bold'),
                        fg='white', cursor='hand2', bg='brown1', height=2, width=25,
                        activebackground='brown1', activeforeground='white', command=login)
loginButton.place(x=565, y=450)


loginWindow.mainloop()
