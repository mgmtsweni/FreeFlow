#!/usr/bin/python3
""" functions which handles management of the employees
    handles also the viewing of the streets camars
    to also launch the the app from this window
"""
from tkinter import *
from tkinter import messagebox
import sqlite3
from vlc import *
import runpy

"""functions"""

def stop_media(event):
    player.destroy()


def launch():
    runpy.run_path('../lights.py')
    

def BreeSmall():
    """Cnr of Bree and Smallfunction"""
    streetframe = Frame(adminframe, width=830, height=656, bg='blue')
    streetframe.place(x=0, y=0)

    backlabel = Button(streetframe, image=bckicon, bd=0, command=user_wall)
    backlabel.place(x=50, y=50)
    
    heading2 = Label(
        streetframe, text='Cnr of Bree and Small', font=('bold', 25))
    heading2.place(x=280, y=80)

    launchApp = Button(streetframe, text='launch', bd=0, cursor='hand2', bg='NavajoWhite3', font=('Arial Sans', 12, 'bold'),
                       activebackground='NavajoWhite3', activeforeground='brown1', command=launch)
    launchApp.place(x=385, y=555)

    streetlabel = Label(adminframe, image=videohold, width=250, height=250)
    streetlabel.place(x=300, y=200)


def BreeKruis():
    """Cnr of Small And Jeppe function"""
    streetframe = Frame(adminframe, width=830, height=656, bg='blue')
    streetframe.place(x=0, y=0)
    
    backlabel = Button(streetframe, image=bckicon, bd=0, command=user_wall)
    backlabel.place(x=50, y=50)

    heading2 = Label(
        streetframe, text='Cnr of Small And Jeppe', font=('bold', 25))
    heading2.place(x=280, y=80)

    streetlabel = Label(adminframe, image=videohold, width=250, height=250)
    streetlabel.place(x=300, y=200)

    launchApp = Button(streetframe, text='launch', bd=0, cursor='hand2', bg='NavajoWhite3', font=('Arial Sans', 12, 'bold'),
                       activebackground='NavajoWhite3', activeforeground='brown1', command=launch)
    launchApp.place(x=385, y=555)


def JeppeKruis():
    """Cnr of Bree and Kruis function"""
    streetframe = Frame(adminframe, width=830, height=656, bg='blue')
    streetframe.place(x=0, y=0)
    
    backlabel = Button(streetframe, image=bckicon, bd=0, command=user_wall)
    backlabel.place(x=50, y=50)

    heading2 = Label(
        streetframe, text='Cnr of Bree and Kruis', font=('bold', 25))
    heading2.place(x=280, y=80)

    streetlabel = Label(adminframe, image=videohold, width=250, height=250)
    streetlabel.place(x=300, y=200)

    launchApp = Button(streetframe, text='launch', bd=0, cursor='hand2', bg='NavajoWhite3', font=('Arial Sans', 12, 'bold'),
                       activebackground='NavajoWhite3', activeforeground='brown1', command=launch)
    launchApp.place(x=385, y=555)


def JeppeSmall():
    """Cnr of Kruis and Jeppe function"""
    streetframe = Frame(adminframe, width=830, height=656, bg='blue')
    streetframe.place(x=0, y=0)
    
    backlabel = Button(streetframe, image=bckicon, bd=0, command=user_wall)
    backlabel.place(x=50, y=50)
    
    heading2 = Label(
        streetframe, text='Cnr of Kruis and Jeppe', font=('bold', 25))
    heading2.place(x=280, y=80)
    streetlabel = Label(adminframe, image=videohold, width=250, height=250)
    streetlabel.place(x=300, y=200)

    launchApp = Button(streetframe, text='launch', bd=0, cursor='hand2', bg='NavajoWhite3', font=('Arial Sans', 12, 'bold'),
                       activebackground='NavajoWhite3', activeforeground='brown1', command=launch)
    launchApp.place(x=385, y=555)


def user_wall():
    """function for the interface window"""
    userframe = Frame(adminframe, width=830, height=656, bg='blue')
    userframe.place(x=0, y=0)
    heading1 = Label(userframe, text='Interface', font=('bold', 25))
    heading1.place(x=370, y=50)
    

    namelabel = Label(userframe, text='Intercections',
                      bg='blue', font=('bold', 15))
    namelabel.place(x=36, y=175)
    manEntry = Button(userframe, text='Cnr of Bree and Small', bd=0, cursor='hand2', font=('Arial Sans', 12, 'bold'),
                      activebackground='NavajoWhite3', activeforeground='brown1', command=BreeSmall)
    manEntry.place(x=36, y=210)
    manEntry = Button(userframe, text='Cnr of Small And Jeppe', bd=0, cursor='hand2', font=('Arial Sans', 12, 'bold'),
                      activebackground='NavajoWhite3', activeforeground='brown1', command=JeppeSmall)
    manEntry.place(x=36, y=260)
    manEntry = Button(userframe, text='Cnr of Bree and Kruis', bd=0, cursor='hand2', font=('Arial Sans', 12, 'bold'),
                      activebackground='NavajoWhite3', activeforeground='brown1', command=BreeKruis)
    manEntry.place(x=36, y=310)
    manEntry = Button(userframe, text='Cnr of Kruis and Jeppe', bd=0, cursor='hand2', font=('Arial Sans', 12, 'bold'),
                      activebackground='NavajoWhite3', activeforeground='brown1', command=JeppeKruis)
    manEntry.place(x=36, y=360)


def man_wall():
    """fnction for the management window"""
    adminWindow.destroy()
    import mangement


def data_wall():
    """function for the data management window"""
    dataframe = Frame(adminframe, width=830, height=656, bg='blue')
    dataframe.place(x=0, y=0)
    heading1 = Label(dataframe, text='Data Center', font=('bold', 15))
    heading1.place(x=370, y=50)

    employeedata = Button(dataframe, text='Emloyee data', bd=0, cursor='hand2', bg='NavajoWhite3', font=('Arial Sans', 12, 'bold'),
                          activebackground='NavajoWhite3', activeforeground='brown1', command=lambda: employeelist())
    employeedata.place(x=15, y=235)

    employeedata = Button(dataframe, text='Street View', bd=0, cursor='hand2', bg='NavajoWhite3', font=('Arial Sans', 12, 'bold'),
                          activebackground='NavajoWhite3', activeforeground='brown1', command=lambda: streetview())
    employeedata.place(x=15, y=295)

    option_street = Label(optionframe, text='', bg='NavajoWhite3')
    option_street.place(x=5, y=455, width=5, height=30)

    def employeelist():
        listframe = Frame(dataframe, width=830, height=656, bg='blue')
        listframe.place(x=0, y=0)
        heading1 = Label(listframe, text='Employee list tab', font=('bold', 15))
        heading1.place(x=370, y=50)

        backlabel = Button(listframe, image=bckicon, bd=0, command=data_wall)
        backlabel.place(x=50, y=50)

        try:
            connection = sqlite3.connect('database/FreeFlow.db')
            cursor = connection.cursor()
        except:
            messagebox.showerror('Error', 'Database connection Error')

        cursor.execute('SELECT *, oid FROM userdata')
        records = cursor.fetchall()
        print(records)

        show_record = ''
        for record in records:
            show_record += str(record[0]) + '\n' + '\n'

        print_list = Label(listframe, text=show_record, font=('bold', 15), fg='White',bg='blue')
        print_list.place(x=50, y=150)

        connection.commit()
        connection.close()

    def streetview():
        streetframe = Frame(dataframe, width=830, height=656, bg='blue')
        streetframe.place(x=0, y=0)
        heading1 = Label(streetframe, text='Street Data', font=('bold', 15))
        heading1.place(x=370, y=50)
        
        backlabel = Button(streetframe, image=bckicon, bd=0, command=data_wall)
        backlabel.place(x=50, y=50)
        
        streetEntry = Button(streetframe, text='Cnr of Bree and Small', bd=0, cursor='hand2', font=('Arial Sans', 12, 'bold'),
                             activebackground='NavajoWhite3', activeforeground='brown1', command=BreeSmall)
        streetEntry.place(x=36, y=210)
        streetEntry = Button(streetframe, text='Cnr of Small And Jeppe', bd=0, cursor='hand2', font=('Arial Sans', 12, 'bold'),
                             activebackground='NavajoWhite3', activeforeground='brown1', command=JeppeSmall)
        streetEntry.place(x=36, y=260)
        streetEntry = Button(streetframe, text='Cnr of Bree and Kruis', bd=0, cursor='hand2', font=('Arial Sans', 12, 'bold'),
                             activebackground='NavajoWhite3', activeforeground='brown1', command=BreeKruis)
        streetEntry.place(x=36, y=310)
        streetEntry = Button(streetframe, text='Cnr of Kruis and Jeppe', bd=0, cursor='hand2', font=('Arial Sans', 12, 'bold'),
                             activebackground='NavajoWhite3', activeforeground='brown1', command=JeppeKruis)
        streetEntry.place(x=36, y=360)


def delete_wall():
    """function to close window after use"""
    for frame in adminframe.winfo_children():
        frame.destroy()


def index():
    """function to take you back to login screen"""
    adminWindow.destroy()
    import login


def logOut():
    """function to close session"""
    adminWindow.destroy()


def hide_indicator():
    """function to change scroll indercator color"""
    option_user.config(bg='NavajoWhite3')
    option_man.config(bg='NavajoWhite3')
    option_data.config(bg='NavajoWhite3')


def indicator(lb, page):
    """function to only allow one indicator to show"""
    hide_indicator()
    lb.config(bg='brown1')
    delete_wall()
    page()


"""oparations"""
adminWindow = Tk()
adminWindow.geometry('1280x720+10+10')
adminWindow.resizable(0, 0)
adminWindow.title('admin tool')

bgimage = PhotoImage(file='images/bg.png')
adminbg = PhotoImage(file='images/adminbg.png')
videohold = PhotoImage(file='images/admin2.png')
openeye = PhotoImage(file='images/openeye.png')
icon = PhotoImage(file='images/myicon.png')
bgdata = PhotoImage(file='images/bgData.png')
bckicon = PhotoImage(file='images/bckicon.png')


bglabel = Label(adminWindow, image=bgimage)
bglabel.place(x=0, y=0)

optionframe = Frame(adminWindow, width=350, height=656, bg='NavajoWhite3')
optionframe.place(x=50, y=50)

adminWindow.bind("<KeyPress-s>", lambda event: stop_media(event))

adminframe = Frame(adminWindow, width=830, height=656, bg='white')
adminframe.place(x=400, y=50)

"""Option manu"""
bgicon = Label(optionframe, image=icon, bd=0)
bgicon.place(x=15, y=25)

optionheading = Label(optionframe, text='Software Management Center', font=('Microsoft Yahei UI Light', 15, 'bold'),
                      bg='NavajoWhite3', fg='brown4')
optionheading.place(x=15, y=175)

userManEntry = Button(optionframe, text='interface', bd=0, cursor='hand2', bg='NavajoWhite3', font=('Arial Sans', 12, 'bold'),
                      activebackground='NavajoWhite3', activeforeground='brown1', command=lambda: indicator(option_user, user_wall))
userManEntry.place(x=15, y=255)

option_user = Label(optionframe, text='', bg='NavajoWhite3')
option_user.place(x=5, y=255, width=5, height=30)


manEntry = Button(optionframe, text='User Management', bd=0, cursor='hand2', bg='NavajoWhite3', font=('Arial Sans', 12, 'bold'),
                  activebackground='NavajoWhite3', activeforeground='brown1', command=lambda: indicator(option_man, man_wall))
manEntry.place(x=15, y=355)

option_man = Label(optionframe, text='', bg='NavajoWhite3')
option_man.place(x=5, y=355, width=5, height=30)


databaseEntry = Button(optionframe, text='Database', bd=0, cursor='hand2',  bg='NavajoWhite3', font=('Arial Sans', 12, 'bold'),
                       activebackground='NavajoWhite3', activeforeground='brown1', command=lambda: indicator(option_data, data_wall))
databaseEntry.place(x=15, y=455)

option_data = Label(optionframe, text='', bg='NavajoWhite3')
option_data.place(x=5, y=455, width=5, height=30)


loginButton = Button(optionframe, text='Log Out', font=('Arial Sans', 8, 'bold'), fg='white', cursor='hand2',
                     bg='brown1', height=2, width=15, activebackground='brown1', activeforeground='white', command=logOut)
loginButton.place(x=15, y=575)

secondButton = Button(optionframe, text='Refrash', font=('Arial Sans', 8, 'bold'), fg='white', cursor='hand2',
                      bg='brown1', height=2, width=15, activebackground='brown1', activeforeground='white', command=index)
secondButton.place(x=165, y=575)

adminWindow.mainloop()
