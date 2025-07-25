from tkinter import *
r=Tk()
r.geometry("500x400")
r.config(bg="black")
def add ():
    n1=int(num1.get())
    n2=int(num2.get())
    sm=n1+n2
    an.config(text=f"Result:{sm}")
def sub():
    n1=int(num1.get())
    n2=int(num2.get())
    sm=n1-n2
    an.config(text=f"Result:{sm}")
def mu():
    n1=int(num1.get())
    n2=int(num2.get())
    sm=n1*n2
    an.config(text=f"Result:{sm}")
def di():
    n1=int(num1.get())
    n2=int(num2.get())
    sm=n1/n2
    an.config(text=f"Result:{sm}")
def fl():
    n1=int(num1.get())
    n2=int(num2.get())
    sm=n1//n2
    an.config(text=f"Result:{sm}")
la=Label(r,text="CALCULATOR",font=("Ravie",40),fg="#00ff00",bg="black")
la.grid(row=0,column=0,columnspan=4)
num1=Entry(r,width=50,bd=10)
num1.grid(row=1,column=0,columnspan=10)
num2=Entry(r,width=50,bd=10)
num2.grid(row=3,column=0,columnspan=4)
ll=Label(r,text="  ",bg="black")
ll.grid(row=5,column=0)
ll=Label(r,text="  ",bg="black")
ll.grid(row=5,column=1)
ad=Button(r,text="+",command=add,padx=20,pady=20,bg="#171716",fg='white')
ad.grid(row=6,column=1)
su=Button(r,text='-',command=sub,padx=20,pady=20,bg='#171716',fg='white')
su.grid(row=6,column=2)
mu=Button(r,text='x',command=mu,padx=20,pady=20,bg='#171716',fg='white')
mu.grid(row=6,column=3)
ll=Label(r,text="  ",bg="black")
ll.grid(row=7,column=1)
di=Button(r,text='/',command=di,padx=20,pady=20,bg='#171716',fg='white')
di.grid(row=8,column=1)
ll=Label(r,text="  ",bg="black")
ll.grid(row=7,column=2)
fl=Button(r,text='//',command=fl,padx=20,pady=20,bg='#171716',fg='white')
fl.grid(row=8,column=2)
ll=Label(r,text="  ",bg="black")
ll.grid(row=7,column=3)
f=Button(r,text='nothing',padx=20,pady=20,bg='#171716',fg='white')
f.grid(row=8,column=3)
an=Label(r,text="result :")
an.grid()
r.mainloop()

