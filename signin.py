# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import psycopg2 as pg


#funct part
def forget_pass():

    def change_password():
        if email_entry.get()=='' or password_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error', 'All Fields Are Required', parent=window)
        elif password_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Error', 'Passwords arent matching', parent=window)
        else:
            conn = pg.connect(host='localhost', database='Pharmacy', port='5432', user='postgres', password='admin')
            mycursor = conn.cursor()

            query = 'select * from userdata where email=%s'
            mycursor.execute(query, (email_entry.get()))
            row = mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error', 'User with this email doesnt exist', parent=window)
            else:
                query='update userdata set password=%s where email=%s'
                mycursor.execute(query, (password_entry.get(), email_entry.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo('Succes', 'Password is reset', parent=window)
                window.destroy()






    window = Toplevel()
    window.geometry('990x660+50+50')
    window.title('Change Password')

    bgPic= ImageTk.PhotoImage(file='backg.jpg')
    bglabel = Label(window, image=bgPic)
    bglabel.grid()

    heading_label = Label(window, text='RESET PASSWORD', font=('Lalita', 20, 'bold'),
                                                             bg='#88D8C0', fg='black')
    heading_label.place(x=480, y=60)

    emailLabel = Label(window, text='Email', font=('Lilita', 14), bd=0, bg='#88D8C0', fg='black')
    emailLabel.place(x=500, y=120)

    email_entry = Entry(window, width=25, font=('Lilita', 12), bd=0, bg='#88D8C0', fg='black')
    email_entry.place(x=500, y=150)

    Frame(window, width=250, height=2, bg='green').place(x=500, y=180)

    passwordLabel = Label(window, text='New Password', font=('Lilita', 14), bd=0, bg='#88D8C0', fg='black')
    passwordLabel.place(x=500, y=210)

    password_entry = Entry(window, width=25, font=('Lilita', 12), bd=0, bg='#88D8C0', fg='black')
    password_entry.place(x=500, y=240)

    Frame(window, width=250, height=2, bg='green').place(x=500, y=270)

    confirmpassLabel = Label(window, text='Confirm Password', font=('Lilita', 14), bd=0, bg='#88D8C0', fg='black')
    confirmpassLabel.place(x=500, y=300)

    confirmpass_entry=Entry(window, width=25, font=('Lilita', 12), bd=0, bg='#88D8C0', fg='black')
    confirmpass_entry.place(x=500, y=330)

    Frame(window, width=250, height=2, bg='green').place(x=500, y=360)

    submitButton = Button(window, text='Submit',font=('Lilita', 16),
                    bg='#88D8C0', fg='blue', cursor='hand2', bd=0, width=15, command=change_password)
    submitButton.place(x=540, y=390)




















def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'All fields are required to fill')

    else:
        try:
            conn = pg.connect(host='localhost', database='Pharmacy', port='5432', user='postgres', password='admin')
            mycursor=conn.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not established')
            return
        mycursor = conn.cursor()
        query='Select * from userdata where username=%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row=mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Welcome', 'Successfully signed to system')






def signup_page():
    login_window.destroy()
    import signup

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0, END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0, END)


#main part
login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(False, False)
login_window.title('Login page')

bgImage = ImageTk.PhotoImage(file='backg.jpg')

bgLabel=Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)

heading=Label(login_window, text='USER LOGIN', font=('Lilita',25, 'bold'), bg='#88D8C0', fg='black')
heading.place(x=660,y=100)

usernameEntry = Entry(login_window, width=25, font=('Lilita', 12), bd=0,bg='#88D8C0', fg='black')
usernameEntry.place(x=650, y=200)
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>', user_enter)

frame1 =Frame(login_window, width=250, height=2, bg='green')
frame1.place(x=640, y=220)

passwordEntry = Entry(login_window, width=25, font=('Lilita', 12), bd=0,bg='#88D8C0', fg='black')
passwordEntry.place(x=650, y=260)
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>', password_enter)


frame2 =Frame(login_window, width=250, height=2, bg='green')
frame2.place(x=640, y=280)

forgetButton =Button(login_window,text='Forget password?', bd=0, bg='#88D8C0',
                     activebackground='#88D8C0', cursor='hand2', font=('Lilita', 10), command=forget_pass)
forgetButton.place(x=780, y=300)

loginButton= Button(login_window, text='Login', font=('Open Sans', 15, 'bold'),
                    bg='#88D8C0', fg='black', cursor='hand2', bd=0, width=20, command=login_user)
loginButton.place(x=640 , y=340)

newaccountButton=Button(login_window, text='Create an account',font=('Lilita', 11, 'underline'),
                    bg='#88D8C0', fg='blue', cursor='hand2', bd=0, width=20, command=signup_page)
newaccountButton.place(x=670, y=380)


login_window.mainloop()

