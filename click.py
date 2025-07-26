#click to count
from tkinter import *
count=0
def inc():
    global count
    count+=1
    label.config(text=f"COUNT:{count}")
win=Tk()
label=Label(win,text="hello",font=("stencil",50))
label.pack()

lb=Button(win,text="click",font=("Stencil",20)command=inc)
lb.pack()

win.mainloop()
