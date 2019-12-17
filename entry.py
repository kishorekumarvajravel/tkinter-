from tkinter import *
import tkinter.messagebox as m
v=Tk()
v.geometry("400x400")

def click():
    ans=e.get()
    m.showinfo("hi",ans)


l=Label(v,text="name")
l.pack(side=LEFT)
e=Entry(v)
e.pack(side=LEFT)
b=Button(v,text="click",command=click)
b.pack(side=LEFT)
mainloop()

