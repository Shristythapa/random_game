from tkinter import *
import random
win=Tk()
win.title("                                                                                                                                        Random")
win.minsize(1000,1000)
win.config(bg="#bf5a52")
win.iconbitmap("random.ico")

lab=Label(win,text="Test Your Luck!!!",bg="#bf5a52",font=("roboto",50,"bold"))
lab.place(x=199,y=5)

one=Button(win,text="ONE",command=lambda:fun(1),font=("roboto",20,"normal"),height=2,width=10,bg="black",fg="white")
one.place(x=100,y=200)

two=Button(win,text="TWO",command=lambda:fun(2),height=2,width=10,font=("roboto",20,"normal"),bg="black",fg="white")
two.place(x=400,y=200)

three=Button(win,text="THREE",command=lambda:fun(3),height=2,width=10,font=("roboto",20,"normal"),bg="black",fg="white")
three.place(x=700,y=200)

four=Button(win,text="FOUR",command=lambda:fun(4),height=2,width=10,font=("roboto",20,"normal"),bg="black",fg="white")
four.place(x=100,y=400)

five=Button(win,text="FIVE",command=lambda:fun(5),height=2,width=10,font=("roboto",20,"normal"),bg="black",fg="white")
five.place(x=400,y=400)

six=Button(win,text="SIX",command=lambda:fun(6),height=2,width=10,font=("roboto",20,"normal"),bg="black",fg="white")
six.place(x=700,y=400)

width=50
height=25
bg="black"

def fun(num):
    lucky= random.randint(1,7)
    if lucky==num:
       top=Toplevel(win,height=500,width=600,bg="red")
       top.geometry("300x150")
       top.minsize(height=300,width=400)
       top.maxsize(height=300,width=400)
       top.minsize(height=300,width=400)
       x = win.winfo_x()
       y = win.winfo_y()
       top.geometry("+%d+%d" %(x+300,y+200))
       top.wm_transient(win)

       label=Label(top,text="You WON!!!",bg="red",fg="black",font=("roboto",25,"normal"))
       label.place(x=100,y=80)

       button=Button(top,text="Exit",width=10,bg="black",fg="red",font=("roboto",20,"normal"),command=top.destroy)
       button.place(x=100,y=150)

       top.mainloop()

    else:
        top2=Toplevel(win,height=500,width=600,bg="black")
        top2.geometry("300x150")
        top2.minsize(height=300,width=400)
        top2.maxsize(height=300,width=400)
        x = win.winfo_x()
        y = win.winfo_y()
        top2.geometry("+%d+%d" %(x+300,y+200))
        top2.wm_transient(win)

        label2=Label(top2,text="You Loose!!!",bg="black",fg="red",font=("roboto",25,"normal"))
        label2.place(x=100,y=80)

        button2=Button(top2,text="Exit",width=10,bg="red",fg="black",font=("roboto",20,"normal"),command=top2.destroy)
        button2.place(x=100,y=150)

        top2.mainloop()


win.mainloop()