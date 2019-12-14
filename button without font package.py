from tkinter import *
v=Tk()
v.geometry("400x400")
v.title("creating button")


#creating a button
b1=Button(v,text="stop",font=("bold",20),width=5,height=1,bg="blue",fg="yellow",activebackground="green",activeforeground="white")

b1.pack()
mainloop()
