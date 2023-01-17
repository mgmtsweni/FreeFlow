#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3


"""functions"""
def clear():
    nameEntry.delete(0, END)
    userNumEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmPassEntry.delete(0,END)
    check1.set(0)
    check2.set(0)
    check.set(0)

def index():
    funcWindow.destroy()
    import admin


def logOut():
    funcWindow.destroy()


def database():
    if nameEntry.get() == '' or userNumEntry.get() == '' or \
            usernameEntry.get() == '' or passwordEntry.get() == '' or confirmPassEntry.get() == '':
        messagebox.showerror('error:', 'all field are required')
    elif  passwordEntry.get() != confirmPassEntry.get():
        messagebox.showerror('error:', 'passwords do not match')
    elif check == 0 or check1 == 0 or check2 == 0:
        messagebox.showerror('error:', 'Check user Postions')
    else:
        try:
            connection = sqlite3.connect('database/FreeFlow.db')
            cursor = connection.cursor()
        except:
            messagebox.showerror('Error','Database connection Error')

    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS userdata (
            name varchar(50),
            usernumber int(20),
            username varchar(50),
            password varchar(20)
        )""")
    except: 
        messagebox.showerror('Error','Database creattion Error')
    
    query = 'SELECT * FROM userdata WHERE username = ? AND usernumber = ?'
    cursor.execute(query,(usernameEntry.get(), userNumEntry.get()))

    row = cursor.fetchone()
    if row != None:
        messagebox.showerror('Error','Data already exist')
    else:
        cursor.execute('INSERT INTO userdata VALUES (:name, :usernumber, :username, :password)',
                {
                    'name': nameEntry.get(),
                    'usernumber':userNumEntry.get(),
                    'username':usernameEntry.get(),
                    'password':passwordEntry.get()
                })
        messagebox.showinfo('Success','User Registered Successful')


    cursor.execute('SELECT * FROM userdata')
    myDB = cursor.fetchall()
    print(myDB)
    
    connection.commit()
    connection.close()
    clear()
        

"""Initiallize App"""
funcWindow = Tk()
funcWindow.geometry('1280x720+10+10')
funcWindow.resizable(0, 0)
funcWindow.title('')


bgimage = PhotoImage(file='images/bgimage.png')
bglabel = Label(funcWindow, image=bgimage)
bglabel.place(x=0, y=0)

loginButton = Button(funcWindow, text='Log Out', font=('Arial Sans', 8, 'bold'), fg='white', cursor='hand2',
                     bg='brown1', height=2, width=15, activebackground='brown1', activeforeground='white', command=logOut)
loginButton.place(x=67, y=628)

secondButton = Button(funcWindow, text='Refrash', font=('Arial Sans', 8, 'bold'), fg='white', cursor='hand2',
                      bg='brown1', height=2, width=15, activebackground='brown1', activeforeground='white', command=index)
secondButton.place(x=217, y=628)

manframe = Frame(funcWindow, width=830, height=656, bg='blue')
manframe.place(x=402, y=53)
heading1 = Label(manframe, text='manage users', font=('bold', 15))
heading1.place(x=370, y=50)

namelabel = Label(manframe, text='Employee Name',
                  bg='blue', font=('bold', 15))
namelabel.place(x=36, y=155)
nameEntry = Entry(manframe, width=24, font=('Microsoft Yahei UI Light', 13, 'bold'),
                  bd=0, fg='black')
nameEntry.insert(0, '')
nameEntry.place(x=40, y=185)

userNumlabel = Label(
    manframe, text='Employee number', bg='blue', font=('bold', 15))
userNumlabel.place(x=36, y=235)
userNumEntry = Entry(manframe, width=24, font=('Microsoft Yahei UI Light', 13, 'bold'),
                     bd=0, fg='black')
userNumEntry.insert(0, '')
userNumEntry.place(x=40, y=265)

usernamelabel = Label(manframe, text='Create Username',
                      bg='blue', font=('bold', 15))
usernamelabel.place(x=36, y=315)
usernameEntry = Entry(manframe, width=24, font=('Microsoft Yahei UI Light', 13, 'bold'),
                      bd=0, fg='black')
usernameEntry.insert(0, '')
usernameEntry.place(x=40, y=345)

passwordlabel = Label(manframe, text='Create Password',
                      bg='blue', font=('bold', 15))
passwordlabel.place(x=36, y=395)
passwordEntry = Entry(manframe, width=24, font=('Microsoft Yahei UI Light', 13, 'bold'),
                      bd=0, fg='black')
passwordEntry.insert(0, '')
passwordEntry.place(x=40, y=425)

confirmPasslabel = Label(
    manframe, text='Confirm Password', bg='blue', font=('bold', 15))
confirmPasslabel.place(x=36, y=475)
confirmPassEntry = Entry(manframe, width=24, font=('Microsoft Yahei UI Light', 13, 'bold'),
                         bd=0, fg='black')
confirmPassEntry.insert(0, '')
confirmPassEntry.place(x=40, y=505)

"""checkboxes"""
check = IntVar()
userStatuslabel = Label(
    manframe, text='Employee Rights', bg='blue', font=('bold', 15),)
userStatuslabel.place(x=500, y=155)

userRights1 = Checkbutton(manframe, text='Management', font=('bold', 15), bg='blue',
                          activebackground='blue', variable=check)
userRights1.place(x=500, y=185)

check1 = IntVar()
userRights2 = Checkbutton(manframe, text='Supervisor', font=('bold', 15), bg='blue',
                          activebackground='blue',variable=check1)
userRights2.place(x=500, y=215)

check2 = IntVar()
userRights3 = Checkbutton(manframe, text='staff', font=('bold', 15), bg='blue',
                          activebackground='blue',variable=check2)
userRights3.place(x=500, y=245)

SubmitButton = Button(manframe, text='submite', font=('Arial Sans', 8, 'bold'), fg='white', cursor='hand2',
                      bg='brown1', height=2, width=20, activebackground='brown1', activeforeground='white', command=database)
SubmitButton.place(x=550, y=575)


"""Run App"""
funcWindow.mainloop()
