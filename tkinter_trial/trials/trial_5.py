import tkinter as tk
from tkinter import *
from tkinter import messagebox

ws =Tk()
ws.title('Scipt-generator')
ws.geometry('1920x1080')
ws.configure(bg='#dddddd')

def selection():
    choice = var.get()
    if choice == 1:
        m = 'Ms.'
        Label(frame, text='Full Name').grid(row=2, column=0, padx=5, pady=5)
        ws.update_idletasks()
    elif choice == 2:
        m = 'Mr.'
    elif choice == 3:
        pass
    elif choice == 4:
        m = 'Ms.'
    elif choice == 5:
        m = 'Mr.'
    elif choice == 6:
        pass
    return m

def submit():
    try:
        name = name_Tf.get()
        m = selection()
        return messagebox.showinfo('PythonGuides', f'{m} {name}, submitted form.')
    except Exception as ep:
        return messagebox.showwarning('PythonGuides', 'Please provide valid input')

def termsCheck():
    if cb.get() == 1:
        submit_btn['state'] = NORMAL
    else:
        submit_btn['state'] = DISABLED
        messagebox.showerror('PythonGuides', 'Accept the terms & conditions')


frame = Label(ws, bg='#dddddd')
frame.pack()
shape = LabelFrame(frame, text='Gender', padx=30, pady=10)

var =IntVar()
cb = IntVar()

# Label(frame, text='Full Name').grid(row=0, column=0, padx=5, pady=5)
# Label(frame, text='Email').grid(row=1, column=0, padx=5, pady=5)
# Label(frame, text='Password').grid(row=2, column=0, padx=5, pady=5)

Radiobutton(shape, text='Semi-Circle', variable=var, value=1,command=selection).grid(row=0, column=1)
Radiobutton(shape, text='PFC', variable=var, value=2,command=selection).grid(row=0, column=2)
Radiobutton(shape, text='I-Beam', variable=var, value=3,command=selection).grid(row=0, column=3)
Radiobutton(shape, text='RHS', variable=var, value=4,command=selection).grid(row=1, column=1)
Radiobutton(shape, text='NACA0025', variable=var, value=5,command=selection).grid(row=1, column=2)
Radiobutton(shape, text='Reid Section', variable=var, value=6,command=selection).grid(row=1, column=3)

# name_Tf = Entry(frame)
# name_Tf.grid(row=0, column=2)
# Entry(frame).grid(row=1, column=2)
# Entry(frame, show="*").grid(row=2, column=2)
shape.grid(row=0, columnspan=3,padx=30)
# Checkbutton(frame, text='Accept the terms & conditions', variable=cb, onvalue=1, offvalue=0,command=termsCheck).grid(row=4, columnspan=4, pady=5)








submit_btn = Button(frame, text="Submit", command=submit, padx=50, pady=5, state=DISABLED)
submit_btn.grid(row=5, columnspan=4, pady=2)

ws.mainloop()
