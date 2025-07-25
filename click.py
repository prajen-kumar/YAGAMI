from tkinter import *
count=0
def inc():
    global count
    count+=1
    label.config(text=f"Count:{count}")
win=Tk()
label=Label(win,text="hello",font=("stencil",50))
label.pack()

lb=Button(win,text="click",command=inc)
lb.pack()

win.mainloop()
