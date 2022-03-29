from tkinter import *
import random
win=Tk()
win.title("Random")

one=Button(win,text="ONE",command=lambda:fun(1))
one.pack()

two=Button(win,text="TWO",command=lambda:fun(2))
two.pack()

three=Button(win,text="THREE",command=lambda:fun(3))
three.pack()

four=Button(win,text="FOUR",command=lambda:fun(4))
four.pack()

five=Button(win,text="FIVE",command=lambda:fun(5))
five.pack()

six=Button(win,text="SIX",command=lambda:fun(6))
six.pack()

def fun(num):
    lucky= random.randint(1,7)
    if lucky==num:
       name=Label(win,text="your lucky!!")
       name.pack()
    else:
        name2=Label(win,text="you failed!!")
        name2.pack()


win.mainloop()