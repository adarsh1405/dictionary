import json
from tkinter import *
from tkinter import simpledialog
from difflib import get_close_matches
data=json.load(open("data.json"))
window=Tk()
def search():
    wrd=value.get()
    wrd=wrd.lower()
    if wrd in data:
        t1.insert(END,data[wrd])
    elif len(get_close_matches(wrd,data.keys()))>0:
        ai=simpledialog.askstring("input string","Did You Mean %s insted ? Enter Y for YES & N for NO: "%get_close_matches(wrd,data.keys())[0])
        if ai=="Y" or ai=="y":
            t1.insert(END,data[get_close_matches(wrd,data.keys())[0]])
        else:
            t1.insert(END,"Didn't Understand .PLEASE RETRY")
    else:
        t1.insert(END,"WORD NOT EXIST!!")
    #t1.insert(END,value.get())
def clear():
    t1.delete('1.0', END)
    t1.update()

value=StringVar()

l1=Label(window,text="WORD :")
l1.grid(row=3,column=2)

e1=Entry(window,textvariable=value)
e1.grid(row=3,column=3)

b1=Button(window,text="Search",command=search)
b1.grid(row=5,column=3)

b2=Button(window,text="clear",command=clear)
b2.grid(row=5,column=6)


t1=Text(window,height=20,width=100)
t1.grid(row=8,column=3)


window.geometry("900x400")
window.mainloop()
