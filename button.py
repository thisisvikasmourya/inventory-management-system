#import all methods from tkinter module

from tkinter import *

from tkinter import messagebox

#create master 

root=Tk()

#set the geometry of window3

root.geometry("100x100")

def info():

#this function will show the information message

    messagebox.showinfo("information","Information")

def error():

#this function will show the warning message    

    messagebox.showwarning("error","Error")

def warn():

#this function will show the error message

    messagebox.showerror("warning","Warning")


#this function will show the askinfo message

def ask():

    messagebox.askquestion("confirm","Are you sure?")

#create and place the button widgets

Info_btn=Button(root,text="info",command=info)
Info_btn.pack()
Error_btn=Button(root,text="error",command=error)
Error_btn.pack()
warn_btn=Button(root,text="warn",command=warn)
warn_btn.pack()
Exit_btn=Button(root,text="exit",command=ask)
Exit_btn.pack()

root.mainloop()
