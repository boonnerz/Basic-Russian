#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
root=Tk()

root.geometry('420x420+200+200')
#stylehead = root.Style()
#stylehead.configure('heading', font='Courier 32')

head = Label(root, text='Russian Basic!',font='Courier 26')
head.place(x=70,y=30)

a=Button(root,justify = LEFT)#button_สอนภาษา
photoa=PhotoImage(file="ruski-g.gif")
a.config(image=photoa,width="110",height="110")
a.place(x=65,y=100)

b=Button(root,justify = LEFT)#button_ความรู้ทั่วไปรัสเซีย
photob=PhotoImage(file="common-g.gif")
b.config(image=photob,width="110",height="110")
b.place(x=245,y=100)

c=Button(root,justify = LEFT)#button_ผู้จัดทำ
photoc=PhotoImage(file="maker-g.gif")
c.config(image=photoc,width="110",height="110")
c.place(x=65,y=260)

d=Button(root,justify = LEFT)#button_ออก
photod=PhotoImage(file="out-g.gif")
d.config(image=photod,width="110",height="110")
d.place(x=245,y=260)



root.mainloop()
