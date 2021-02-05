import pyjokes
from tkinter import ttk  
import tkinter
from tkinter import *
from tkinter import messagebox
root=tkinter.Tk()
root.geometry("700x400+350+300")
root.resizable(0,0)
x="TRUE"
b=pyjokes.get_joke(language = "en",category = "all")
def jk():
    global a,x
    if x == "TRUE":
        a = pyjokes.get_joke(language = "en",category = "neutral")
        c.config(text=a)
def nex():
    global b
    c.config(text=b)

v = Label(root,text="JOKE TALES",bg="grey",width=50,height=1,
         font=('sans-serif',23),fg="orange")
v.pack()
c = Label(root,text="Press below button To Display Joke",bg = "grey",height =15,width =150)
c.pack(padx=2,pady=10)
v1 = Label(root,text="Hope you find Intresting",bg="grey",width=150,height=1,
         font=('sans-serif',15),fg="orange")
v1.pack()
btn = Frame(root)
btn.pack()
bu = Button(btn,text="previous",command=nex)
bu.pack(side=LEFT,padx=20,pady=10)
bu = Button(btn,text="Joke",command=jk)
bu.pack(side=LEFT,padx=50)

v2 = Label(root,text="© Joke Tales",width=150,height=10,
         font=('sans-serif',12),fg="orange",bg="grey")
v2.pack(side =BOTTOM)
root.mainloop()
