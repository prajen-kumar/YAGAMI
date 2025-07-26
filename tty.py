#FLAMES PROJECT..
from tkinter import *
oo=Tk()
oo.geometry('800x900')
oo.title("FLAMES CALCULATOR")
# \\U0001F970
ph=PhotoImage(file="z://KHALIQUE AHMED//MYSQL BATCH//C151//emoj.PNG")
oo.config(background="#cc0c0c")
#defining function:
def flames_game():
    name1=l1.get()
    name2=l2.get()
    name1=name1.replace(' ',' ').lower()
    name2=name2.replace(' ',' ').lower()
    list1=list(name1)
    list2=list(name2)
    for char in name1:
        if char in list2:
            list2.remove(char)
            list1.remove(char)
    remaining = len(list1)+len(list2)
    flames=['F','L','A','M','E','S']
    while len(flames)>1:
        index=(remaining %len(flames))-1
        if index >=0:
            flames=flames[index+1:]+flames[:index]
        else:
            flames=flames[:len(flames)-1]
    result=flames[0]
    if (result=='F'):
        print(name1,'and ',name2,'-',"FRIENDS","\U0001f60e")
        r0t="FRIENDS \U0001f60e"
        tyt.config(text=f"{r0t}")
    elif (result=='L'):
        print(name1,'and ',name2,'-',"LOVE","\u2764")
        r0t="LOVE \u2764"
        tyt.config(text=f"{r0t}")
    elif (result=='A'):
        print(name1,'and ',name2,'-',"AFFECTION","\U0001f44d")
        r0t="AFFECTION \U0001f44d"
        tyt.config(text=f"{r0t}")
    elif (result=='M'):
        print(name1,'and ',name2,'-',"MARRIAGE","\U0001f600")
        r0t="MARRIAGE \U0001f600"
        tyt.config(text=f"{r0t}")
    elif (result=='E'):
        print(name1,'and ',name2,'-',"ENIMIES ","\U0001F606")
        r0t="ENIMIES \U0001F606"
        tyt.config(text=f"{r0t}")
    elif (result=='S'):
        print(name1,'and ',name2,'-',"SIBLINGS","\U0001f602")
        r0t="SIBLINGS \U0001f602"
        tyt.config(text=f"{r0t}")
#creation of label:
ru=Label(oo,text="Relationship Calculator",font=("Ravie",25),bg="#cc0c0c",fg='white',
         image=ph,compound="top")
ru.grid(row=0,column=3)
r=Label(oo,text="first name:",bg="#cc0c0c",fg="#d5d9d4",font=("stencil",20),padx=10,pady=10)
r.grid(row=2,column=2)
#creation of entry:
l1=Entry(oo,bd=10,font=("Snap ITC",20))
l1.grid(row=2,column=3)
ent=Label(text="  " ,bg="#cc0c0c")
ent.grid(row=3,column=3)
r2=Label(oo,text="second name:",bg="#cc0c0c",fg="#d5d9d4",font=("stencil",20),padx=10,pady=10)
r2.grid(row=4,column=2)
l2=Entry(oo,bd=10,font=("Snap ITC",20))
l2.grid(row=4,column=3)
ent=Label(text="  " ,bg="#cc0c0c")
ent.grid(row=5,column=3)
#creation of button:
b=Button(oo,text="submit",bd=10,command=flames_game,activeforeground="red",
         activebackground="white",fg="white",bg="red",font=("Latin",30))
b.grid(row=6,column=3)
tyt=Label(text="RESULT :",fg="white",bg="red",font=("stencil",25))
tyt.grid(row=7,column=1)
oo.mainloop()
