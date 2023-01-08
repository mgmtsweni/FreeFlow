#!/usr/bin/python3
from tkinter import *


"""functions"""

def BreeSmall():
    """Cnr of Bree and Small"""
    streetframe = Frame(adminframe, width=830, height=656, bg='blue')
    streetframe.place(x=0, y=0)
    
    heading2 = Label(streetframe, text='Cnr of Bree and Small', font=('bold', 25))
    heading2.place(x=280, y=80)
    
    streetlabel = Label(adminframe, image=videohold, width=250, height=250)
    streetlabel.place(x=300, y=200)

def BreeKruis():
    """Cnr of Small And Jeppe"""
    streetframe = Frame(adminframe, width=830, height=656, bg='blue')
    streetframe.place(x=0, y=0)
    
    heading2 = Label(streetframe, text='Cnr of Small And Jeppe', font=('bold', 25))
    heading2.place(x=280, y=80)
    
    streetlabel = Label(adminframe, image=videohold, width=250, height=250)
    streetlabel.place(x=300, y=200)

def JeppeKruis():
    """Cnr of Bree and Kruis"""
    streetframe = Frame(adminframe, width=830, height=656, bg='blue')
    streetframe.place(x=0, y=0)
    
    heading2 = Label(streetframe, text='Cnr of Bree and Kruis', font=('bold', 25))
    heading2.place(x=280, y=80)
    
    streetlabel = Label(adminframe, image=videohold, width=250, height=250)
    streetlabel.place(x=300, y=200)

def JeppeSmall():
    """Cnr of Kruis and Jeppe"""
    streetframe = Frame(adminframe, width=830, height=656, bg='blue')
    streetframe.place(x=0, y=0)
    heading2 = Label(streetframe, text='Cnr of Kruis and Jeppe', font=('bold', 25))
    heading2.place(x=280, y=80)
    streetlabel = Label(adminframe, image=videohold, width=250, height=250)
    streetlabel.place(x=300, y=200)



def user_wall():
    userframe = Frame(adminframe, width=830, height=656, bg='blue')
    userframe.place(x=0, y=0)
    heading1 = Label(userframe, text='Interface', font=('bold', 25))
    heading1.place(x=370, y=50)

    namelabel = Label(userframe, text='Intercections', bg='blue', font=('bold', 15))
    namelabel.place(x=36, y=175)
    manEntry = Button(userframe, text='Cnr of Bree and Small', bd=0, cursor='hand2', font=('Arial Sans', 12, 'bold'),
                      activebackground='NavajoWhite3', activeforeground='brown1', command=BreeSmall)
    manEntry.place(x=36, y=210)
    manEntry = Button(userframe, text='Cnr of Small And Jeppe', bd=0, cursor='hand2', font=('Arial Sans', 12, 'bold'),
                      activebackground='NavajoWhite3', activeforeground='brown1', command= JeppeSmall)
    manEntry.place(x=36, y=260)
    manEntry = Button(userframe, text='Cnr of Bree and Kruis', bd=0, cursor='hand2', font=('Arial Sans', 12, 'bold'),
                      activebackground='NavajoWhite3', activeforeground='brown1', command=BreeKruis)
    manEntry.place(x=36, y=310)
    manEntry = Button(userframe, text='Cnr of Kruis and Jeppe', bd=0, cursor='hand2', font=('Arial Sans', 12, 'bold'),
                      activebackground='NavajoWhite3', activeforeground='brown1', command=JeppeKruis)
    manEntry.place(x=36, y=360)


def man_wall():
    manframe = Frame(adminframe, width=830, height=656, bg='blue')
    manframe.place(x=0, y=0)
    heading1 = Label(manframe, text='manage users', font=('bold', 15))
    heading1.place(x=370, y=50)

    namelabel = Label(manframe, text='Employee Name',
                      bg='blue', font=('bold', 15))
    namelabel.place(x=36, y=155)
    nameEntry = Entry(manframe, width=24, font=('Microsoft Yahei UI Light', 13, 'bold'),
                      bd=0, fg='black')
    nameEntry.insert(0, '')
    nameEntry.place(x=40, y=185)

    usernamelabel = Label(manframe, text='Create Username',
                          bg='blue', font=('bold', 15))
    usernamelabel.place(x=36, y=235)
    usernameEntry = Entry(manframe, width=24, font=('Microsoft Yahei UI Light', 13, 'bold'),
                          bd=0, fg='black')
    usernameEntry.insert(0, '')
    usernameEntry.place(x=40, y=265)

    passwordlabel = Label(manframe, text='Create Password',
                          bg='blue', font=('bold', 15))
    passwordlabel.place(x=36, y=315)
    passwordEntry = Entry(manframe, width=24, font=('Microsoft Yahei UI Light', 13, 'bold'),
                          bd=0, fg='black')
    passwordEntry.insert(0, '')
    passwordEntry.place(x=40, y=345)

    userNumberlabel = Label(
        manframe, text='Employee Number', bg='blue', font=('bold', 15))
    userNumberlabel.place(x=36, y=395)
    userNumberEntry = Entry(manframe, width=24, font=('Microsoft Yahei UI Light', 13, 'bold'),
                            bd=0, fg='black')
    userNumberEntry.insert(0, '')
    userNumberEntry.place(x=40, y=425)

    userStatuslabel = Label(
        manframe, text='Employee Postion', bg='blue', font=('bold', 15))
    userStatuslabel.place(x=36, y=475)
    userStatusEntry = Entry(manframe, width=24, font=('Microsoft Yahei UI Light', 13, 'bold'),
                            bd=0, fg='black')
    userStatusEntry.insert(0, '')
    userStatusEntry.place(x=40, y=505)

    userStatuslabel = Label(
        manframe, text='Employee Rights', bg='blue', font=('bold', 15),)
    userStatuslabel.place(x=500, y=155)
    userRights1 = Checkbutton(manframe, text='Management', font=('bold', 15), bg='blue',
                              activebackground='blue')
    userRights1.place(x=500, y=185)

    userRights2 = Checkbutton(manframe, text='Supervisor', font=('bold', 15), bg='blue',
                              activebackground='blue')
    userRights2.place(x=500, y=215)

    userRights3 = Checkbutton(manframe, text='staff', font=('bold', 15), bg='blue',
                              activebackground='blue')
    userRights3.place(x=500, y=245)

    SubmitButton = Button(manframe, text='submite', font=('Arial Sans', 8, 'bold'), fg='white', cursor='hand2',
                          bg='brown1', height=2, width=20, activebackground='brown1', activeforeground='white')
    SubmitButton.place(x=550, y=575)


def data_wall():
    dataframe = Frame(adminframe, width=830, height=656, bg='blue')
    dataframe.place(x=0, y=0)
    heading1 = Label(dataframe, text='data', font=('bold', 15))
    heading1.place(x=370, y=50)


def delete_wall():
    for frame in adminframe.winfo_children():
        frame.destroy()


def index():
    adminWindow.destroy()
    import login


def logOut():
    adminWindow.destroy()


def hide_indicator():
    option_user.config(bg='NavajoWhite3')
    option_man.config(bg='NavajoWhite3')
    option_data.config(bg='NavajoWhite3')


def indicator(lb, page):
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

bglabel = Label(adminWindow, image=bgimage)
bglabel.place(x=0, y=0)

optionframe = Frame(adminWindow, width=350, height=656, bg='NavajoWhite3')
optionframe.place(x=50, y=50)

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
