from tkinter import *
# from tkinter.ttk import *
from time import strftime
from datetime import datetime

root=Tk()
root.title('Digital Clock')
root.configure(bg='black')
root.geometry('540x180')

# root.wm_iconbitmap('library/11.ico')

def time1():
    string= strftime('%H:%M:%S %p')
    lable.config(text=string)
    lable.after(1,time1)

lable=Label(root,font=('ds-digital',80),bg='black',fg='cyan')
lable.pack(side=TOP,fill=X)
time1()

date = datetime.now()
exactTime = strftime("%A   %d/%m/%Y")

Label(root,text=f"{exactTime}",font=('ds-digital',40),fg='cyan',bg='black').pack(side=TOP,fill=X)


root.mainloop()