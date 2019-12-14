from tkinter import *
import tkinter.font as font
v=Tk()
v.geometry("40x40")
v.title("count")

#changing button text size
f=font.Font(family='times',size=10,weight='bold')

#creating a button
b1=Button(v,text="stop",width=5,height=1,bg="blue",fg="yellow",activebackground="green",activeforeground="white")

#assign the size to button
b1['font']=f
b1.pack()
mainloop()
