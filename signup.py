from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import psycopg2 as pg

def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    check.set(0)

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All fields should be filled')
    elif  passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Password doesnt match')
    elif check.get()==0:
        messagebox.showerror('Error','Please accept Terms and Conditions')
    else:
        try:
            conn=pg.connect(host='localhost',database='Pharmacy', port='5432', user='postgres', password='admin')
            mycursor=conn.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not established')
            return

        mycursor = conn.cursor()
        query='Select * from userdata where email = %s'
        mycursor.execute(query, (emailEntry.get(),))
        row=mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Email Already Exists')
        else:
            query = 'INSERT INTO userdata(email, username, password) VALUES (%s, %s, %s)'
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('Succes', 'Registration is successful')
            clear()
            signup_window.destroy()
            import signin



def login_page():
    signup_window.destroy()
    import signin


signup_window=Tk()
signup_window.geometry('990x660+50+50')
signup_window.title('Signin Window')
signup_window.resizable(False, False)

background=ImageTk.PhotoImage(file='backg.jpg')

bgLabel=Label(signup_window, image=background)
bgLabel.grid()

frame=Frame(signup_window, width=50, height=20, bg='#88D8C0')
frame.place(x=660, y=160)

heading=Label(signup_window, text='CREATE AN ACCOUNT', font=('Lalita', 20, 'bold'),
                                                             bg='#88D8C0', fg='black')
heading.place(x=620, y=100)

emailLabel=Label(frame, text='Email', font=('Lalita', 10, 'bold'), bg='#88D8C0')
emailLabel.grid(row=1, column=0, sticky='w', padx=25)

emailEntry=Entry(frame, width=30,  font=('Lalita', 10, 'bold'))
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

usernameLabel=Label(frame, text='Username', font=('Lalita', 10, 'bold'), bg='#88D8C0')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25)

usernameEntry=Entry(frame, width=30,  font=('Lalita', 10, 'bold'))
usernameEntry.grid(row=4, column=0, sticky='w', padx=25)

passwordLabel=Label(frame, text='Password', font=('Lalita', 10, 'bold'), bg='#88D8C0')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25)

passwordEntry=Entry(frame, width=30,  font=('Lalita', 10, 'bold'))
passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

confirmLabel=Label(frame, text='Confirm Password', font=('Lalita', 10, 'bold'), bg='#88D8C0')
confirmLabel.grid(row=7, column=0, sticky='w', padx=25)

confirmEntry=Entry(frame, width=30,  font=('Lalita', 10, 'bold'))
confirmEntry.grid(row=8, column=0, sticky='w', padx=25)

check=IntVar()
termsandconditions=Checkbutton(frame, text='I agree to the Terms and Conditions',
                               font=('Lalita', 10, 'bold'), bg='#88D8C0', variable=check)
termsandconditions.grid(row=9, column=0, pady=10)

signupButton=Button(frame, text='Signup',font=('Lalita',15, 'bold'), bg='#88D8C0', command=connect_database)
signupButton.grid(row=10, column=0, pady=10)

alreadyaccount= Label(frame,text='Already have an account?', font=('Lalita',11,), bg='#88D8C0')
alreadyaccount.grid(row=11, column=0, sticky='w', padx=25, pady=10)

loginButton=Button(frame, text='Login', font=('Lalita',10),
                   command=login_page, bg='skyblue')
loginButton.place(x=210, y=285)





signup_window.mainloop()