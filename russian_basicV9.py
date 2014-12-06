#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *
import winsound

def main():#Main Menu
    def btn1():
        root.destroy()
        russian()
    def btn2():
        root.destroy()
        history()
    def btn3():
        root.destroy()
        credit()
    def btn4():
        root.destroy()
        
    root=Tk()

    root.geometry('420x420+200+200')#Menu Frame

    head = Label(root, text='Russian Basic!',font='Courier 26')
    head.place(x=70,y=30)

    a=Button(root,justify = LEFT,command = btn1)#button_russian
    photoa=PhotoImage(file="ruski-g.gif")
    a.config(image=photoa,width="110",height="110")
    a.place(x=65,y=100)

    b=Button(root,justify = LEFT,command = btn2)#button_history
    photob=PhotoImage(file="common-g.gif")
    b.config(image=photob,width="110",height="110")
    b.place(x=245,y=100)

    c=Button(root,justify = LEFT,command = btn3)#button_credit
    photoc=PhotoImage(file="maker-g.gif")
    c.config(image=photoc,width="110",height="110")
    c.place(x=65,y=260)

    d=Button(root,justify = LEFT,command = btn4)#button_exit
    photod=PhotoImage(file="out-g.gif")
    d.config(image=photod,width="110",height="110")
    d.place(x=245,y=260)

    root.mainloop()

'''------------------------------------russian page-------------------------'''
def russian():
    def btn_1():
        root.destroy()
        main()
    def btn_1_wrd():
        root.destroy()
        russian_wrd1()
    def btn_1_nu():
        root.destroy()
        russian_nu()
    def btn_1_tb():
        root.destroy()
        russian_tb()
        
    root=Tk()

    root.geometry('420x420+200+200')#Menu Frame
    head = Label(root, text='Basic Words!',font='Courier 26')
    head.place(x=70,y=30)

    a=Button(root,justify = LEFT,command = btn_1_wrd)#button_words
    photoa=PhotoImage(file="word-g.gif")
    a.config(image=photoa,width="110",height="110")
    a.place(x=65,y=100)

    b=Button(root,justify = LEFT,command = btn_1_nu)#button_numbers
    photob=PhotoImage(file="number-g.gif")
    b.config(image=photob,width="110",height="110")
    b.place(x=245,y=100)

    c=Button(root,justify = LEFT,command = btn_1_tb)#button_table
    photoc=PhotoImage(file="alphabet-g.gif")
    c.config(image=photoc,width="110",height="110")
    c.place(x=65,y=260)

    a=Button(root,justify = LEFT, command = btn_1, text ='Back')#button_russian
    a.place(x=350,y=370)

    root.mainloop()

'''==================================== russian word page 1==========================='''

def russian_wrd1():
    def btn_3():
        root.destroy()
        russian()
    def btn_3_p():
        root.destroy()
        russian_wrd2()
    def btn_3_n():
        root.destroy()
        russian_wrd2()
    def button_1():
        winsound.PlaySound('thx.wav',1)
        word1.config(text="สปา-ซี-บะ")
        word2.config(text="Спасибо")
    def button_2():
        winsound.PlaySound('plz.wav',1)
        word1.config(text="ปา-เชา-สตะ")
        word2.config(text="Пожалуйста")
    def button_3():
        winsound.PlaySound('yes.wav',1)
        word1.config(text="ดา")
        word2.config(text="Да")
    def button_4():
        winsound.PlaySound('no.wav',1)
        word1.config(text="เนียต")
        word2.config(text="Нет")
    def button_5():
        winsound.PlaySound('hello.wav',1)
        word1.config(text="สดราส-สตู-เทีย")
        word2.config(text="Здравствуйте")
    def button_6():
        winsound.PlaySound('hi.wav',1)
        word1.config(text="ปรี-เวียต")
        word2.config(text="Привет")
        
    root=Tk()

    root.geometry('420x420+200+200')#Menu Frame
    head = Label(root, text='ภาษาในชีวิตประจำวัน',font='Courier 26')
    head.pack()

    a=Button(root,justify = LEFT,command=button_1)#button_1
    photoa=PhotoImage(file="word1.gif")
    a.config(image=photoa,width="105",height="80")
    a.place(x=20,y=70)

    b=Button(root,justify = LEFT,command=button_2)#button_2
    photob=PhotoImage(file="word2.gif")
    b.config(image=photob,width="105",height="80")
    b.place(x=150,y=70)

    c=Button(root,justify = LEFT,command=button_3)#button_3
    photoc=PhotoImage(file="word3.gif")
    c.config(image=photoc,width="105",height="80")
    c.place(x=280,y=70)

    d=Button(root,justify = LEFT,command=button_4)#button_4
    photod=PhotoImage(file="word4.gif")
    d.config(image=photod,width="105",height="80")
    d.place(x=20,y=170)

    e=Button(root,justify = LEFT,command=button_5)#button_5
    photoe=PhotoImage(file="word5.gif")
    e.config(image=photoe,width="105",height="80")
    e.place(x=150,y=170)

    f=Button(root,justify = LEFT,command=button_6)#button_6
    photof=PhotoImage(file="word6.gif")
    f.config(image=photof,width="105",height="80")
    f.place(x=280,y=170)

    word1 = Label(root, text='คำอ่าน',font='Courier 14')
    word1.place(x=20, y=290)

    word2 = Label(root, text='คำรัสเซีย',font='Courier 14')
    word2.place(x=20, y=320)


    j=Button(root,justify = LEFT, command = btn_3, text ='Back')#button_main
    j.place(x=350,y=370)

    k=Button(root,justify = LEFT, command = btn_3_p, text ='<<', state=DISABLED)#button_nu_Ppage
    k.place(x=260,y=370)

    l=Button(root,justify = LEFT, command = btn_3_n, text ='>>')#button_nu_Npage
    l.place(x=300,y=370)

        
    root.mainloop()


'''==================================== russian word page 2==========================='''

def russian_wrd2():
    def btn_3():
        root.destroy()
        russian()
    def btn_3_p():
        root.destroy()
        russian_wrd1()
    def btn_3_n():
        root.destroy()
        russian_wrd3()
    def button_7():
        winsound.PlaySound('my name is...wav',1)
        word1.config(text="เมน-ยา-ซา-วูต")
        word2.config(text="Меня зовут ...")
    def button_8():
        winsound.PlaySound('what is your name.wav',1)
        word1.config(text="คัค-วาส-ซา-วูต")
        word2.config(text="Как вас зовут?")
    def button_9():
        winsound.PlaySound('good.wav',1)
        word1.config(text="ฮา-รัช-โช")
        word2.config(text="Хорошо")
    def button_10():
        winsound.PlaySound('bad.wav',1)
        word1.config(text="โพล-ฮะ")
        word2.config(text="Плохо")
    def button_11():
        winsound.PlaySound('please to meet u.wav',1)
        word1.config(text="โอะ-ชิน-ปริ-ยาต-หนะ")
        word2.config(text="Очень приятно")

    root=Tk()

    root.geometry('420x420+200+200')#Menu Frame
    head = Label(root, text='ภาษาในชีวิตประจำวัน',font='Courier 26')
    head.pack()

    a=Button(root,justify = LEFT, command=button_7)#button_7
    photoa=PhotoImage(file="word7.gif")
    a.config(image=photoa,width="105",height="80")
    a.place(x=20,y=70)

    b=Button(root,justify = LEFT, command=button_8)#button_8
    photob=PhotoImage(file="word8.gif")
    b.config(image=photob,width="105",height="80")
    b.place(x=150,y=70)

    c=Button(root,justify = LEFT, command=button_9)#button_9
    photoc=PhotoImage(file="word10.gif")
    c.config(image=photoc,width="105",height="80")
    c.place(x=280,y=70)

    d=Button(root,justify = LEFT, command=button_10)#button_10
    photod=PhotoImage(file="word11.gif")
    d.config(image=photod,width="105",height="80")
    d.place(x=20,y=170)

    e=Button(root,justify = LEFT, command=button_11)#button_11
    photoe=PhotoImage(file="word9.gif")
    e.config(image=photoe,width="155",height="80")
    e.place(x=150,y=170)

    word1 = Label(root, text='คำอ่าน',font='Courier 14')
    word1.place(x=20, y=290)

    word2 = Label(root, text='คำรัสเซีย',font='Courier 14')
    word2.place(x=20, y=320)

    j=Button(root,justify = LEFT, command = btn_3, text ='Back')#button_main
    j.place(x=350,y=370)

    k=Button(root,justify = LEFT, command = btn_3_p, text ='<<')#button_nu_Ppage
    k.place(x=260,y=370)

    l=Button(root,justify = LEFT, command = btn_3_n, text ='>>')#button_nu_Npage
    l.place(x=300,y=370)
        
    root.mainloop()

'''==================================== russian word page 3==========================='''

def russian_wrd3():
    def btn_3():
        root.destroy()
        russian()
    def btn_3_p():
        root.destroy()
        russian_wrd2()
    def btn_3_n():
        root.destroy()
        russian_wrd2()
    def button_12():
        winsound.PlaySound('understand.wav',1)
        word1.config(text="ปา-นิ-มา-เนีย")
        word2.config(text="понимаю")
    def button_13():
        winsound.PlaySound('not understand.wav',1)
        word1.config(text="นี-ปา-นิ-มา-เนีย")
        word2.config(text="не понимаю")
    def button_14():
        winsound.PlaySound('goodbye.wav',1)
        word1.config(text="ดา-สวิ-ดา-เนีย")
        word2.config(text="До свидания")
    def button_15():
        winsound.PlaySound('bye.wav',1)
        word1.config(text="ปัก-กา")
        word2.config(text="Пока")
    def button_16():
        winsound.PlaySound('how are u.wav',1)
        word1.config(text="คัค-เด-ละ")
        word2.config(text="Как дела?")
        
    root=Tk()

    root.geometry('420x420+200+200')#Menu Frame
    head = Label(root, text='ภาษาในชีวิตประจำวัน',font='Courier 26')
    head.pack()

    a=Button(root,justify = LEFT, command=button_12)#button_12
    photoa=PhotoImage(file="word12.gif")
    a.config(image=photoa,width="105",height="80")
    a.place(x=20,y=70)

    b=Button(root,justify = LEFT, command=button_13)#button_13
    photob=PhotoImage(file="word13.gif")
    b.config(image=photob,width="105",height="80")
    b.place(x=150,y=70)

    c=Button(root,justify = LEFT, command=button_14)#button_14
    photoc=PhotoImage(file="word14.gif")
    c.config(image=photoc,width="105",height="80")
    c.place(x=280,y=70)

    d=Button(root,justify = LEFT, command=button_15)#button_15
    photod=PhotoImage(file="word15.gif")
    d.config(image=photod,width="105",height="80")
    d.place(x=20,y=170)

    e=Button(root,justify = LEFT, command=button_16)#button_16
    photoe=PhotoImage(file="word16.gif")
    e.config(image=photoe,width="155",height="80")
    e.place(x=150,y=170)

    word1 = Label(root, text='คำอ่าน',font='Courier 14')
    word1.place(x=20, y=290)

    word2 = Label(root, text='คำรัสเซีย',font='Courier 14')
    word2.place(x=20, y=320)

    j=Button(root,justify = LEFT, command = btn_3, text ='Back')#button_main
    j.place(x=350,y=370)

    k=Button(root,justify = LEFT, command = btn_3_p, text ='<<')#button_nu_Ppage
    k.place(x=260,y=370)

    l=Button(root,justify = LEFT, command = btn_3_n, text ='>>', state=DISABLED)#button_nu_Npage
    l.place(x=300,y=370)
        
    root.mainloop()


'''----------------------------number page 1--------------------------------'''
def russian_nu():
    def btn_3():
        root.destroy()
        russian()
    def btn_3_p():
        root.destroy()
        russian_nu2()
    def btn_3_n():
        root.destroy()
        russian_nu2()
    def play0():
        winsound.PlaySound('0-Audio Track.wav',1)
    def play1():
        winsound.PlaySound('01-Audio Track.wav',1)
    def play2():
        winsound.PlaySound('02-Audio Track.wav',1)
    def play3():
        winsound.PlaySound('03-Audio Track.wav',1)
    def play4():
        winsound.PlaySound('04-Audio Track.wav',1)
    def play5():
        winsound.PlaySound('05-Audio Track.wav',1)
    def play6():
        winsound.PlaySound('06-Audio Track.wav',1)
    def play7():
        winsound.PlaySound('07-Audio Track.wav',1)
    def play8():
        winsound.PlaySound('08-Audio Track.wav',1)
        
        
        
    root=Tk()

    root.geometry('420x420+200+200')#Menu Frame
    head = Label(root, text='เลข Russia',font='Courier 26')
    head.pack()

    a=Button(root,justify = LEFT,command=play0)#button_0
    photoa=PhotoImage(file="num0.gif")
    a.config(image=photoa,width="70",height="70")
    a.place(x=60,y=70)

    b=Button(root,justify = LEFT,command=play1)#button_1
    photob=PhotoImage(file="num1.gif")
    b.config(image=photob,width="70",height="70")
    b.place(x=170,y=70)

    c=Button(root,justify = LEFT,command=play2)#button_2
    photoc=PhotoImage(file="num2.gif")
    c.config(image=photoc,width="70",height="70")
    c.place(x=280,y=70)

    d=Button(root,justify = LEFT,command=play3)#button_3
    photod=PhotoImage(file="num3.gif")
    d.config(image=photod,width="70",height="70")
    d.place(x=60,y=170)

    e=Button(root,justify = LEFT,command=play4)#button_4
    photoe=PhotoImage(file="num4.gif")
    e.config(image=photoe,width="70",height="70")
    e.place(x=170,y=170)

    f=Button(root,justify = LEFT,command=play5)#button_5
    photof=PhotoImage(file="num5.gif")
    f.config(image=photof,width="70",height="70")
    f.place(x=280,y=170)

    g=Button(root,justify = LEFT,command=play6)#button_6
    photog=PhotoImage(file="num6.gif")
    g.config(image=photog,width="70",height="70")
    g.place(x=60,y=270)

    h=Button(root,justify = LEFT,command=play7)#button_7
    photoh=PhotoImage(file="num7.gif")
    h.config(image=photoh,width="70",height="70")
    h.place(x=170,y=270)

    i=Button(root,justify = LEFT,command=play8)#button_8
    photoi=PhotoImage(file="num8.gif")
    i.config(image=photoi,width="70",height="70")
    i.place(x=280,y=270)

    j=Button(root,justify = LEFT, command = btn_3, text ='Back')#button_main
    j.place(x=350,y=370)

    k=Button(root,justify = LEFT, command = btn_3_p, text ='<<', state=DISABLED)#button_nu_Ppage
    k.place(x=260,y=370)

    l=Button(root,justify = LEFT, command = btn_3_n, text ='>>')#button_nu_Npage
    l.place(x=300,y=370)
        
    root.mainloop()

    
'''----------------------------number page 2--------------------------------'''


def russian_nu2():
    def btn_3():
        root.destroy()
        russian()
    def btn_3_p():
        root.destroy()
        russian_nu()
    def btn_3_n():
        root.destroy()
        russian_nu3()
    def play9():
        winsound.PlaySound('09-Audio Track.wav',1)
    def play10():
        winsound.PlaySound('10-Audio Track.wav',1)
    def play11():
        winsound.PlaySound('11-Audio Track.wav',1)
    def play12():
        winsound.PlaySound('12-Audio Track.wav',1)
    def play13():
        winsound.PlaySound('13-Audio Track.wav',1)
    def play14():
        winsound.PlaySound('14-Audio Track.wav',1)
    def play15():
        winsound.PlaySound('15-Audio Track.wav',1)
    def play16():
        winsound.PlaySound('16-Audio Track.wav',1)
    def play17():
        winsound.PlaySound('17-Audio Track.wav',1)
        
        
    root=Tk()

    root.geometry('420x420+200+200')#Menu Frame
    head = Label(root, text='เลข Russia',font='Courier 26')
    head.pack()

    a=Button(root,justify = LEFT,command=play9)#button_9
    photoa=PhotoImage(file="num9.gif")
    a.config(image=photoa,width="70",height="70")
    a.place(x=60,y=70)

    b=Button(root,justify = LEFT,command=play10)#button_10
    photob=PhotoImage(file="num10.gif")
    b.config(image=photob,width="70",height="70")
    b.place(x=170,y=70)

    c=Button(root,justify = LEFT,command=play11)#button_11
    photoc=PhotoImage(file="num11.gif")
    c.config(image=photoc,width="70",height="70")
    c.place(x=280,y=70)

    d=Button(root,justify = LEFT,command=play12)#button_12
    photod=PhotoImage(file="num12.gif")
    d.config(image=photod,width="70",height="70")
    d.place(x=60,y=170)

    e=Button(root,justify = LEFT,command=play13)#button_13
    photoe=PhotoImage(file="num13.gif")
    e.config(image=photoe,width="70",height="70")
    e.place(x=170,y=170)

    f=Button(root,justify = LEFT,command=play14)#button_14
    photof=PhotoImage(file="num14.gif")
    f.config(image=photof,width="70",height="70")
    f.place(x=280,y=170)

    g=Button(root,justify = LEFT,command=play15)#button_15
    photog=PhotoImage(file="num15.gif")
    g.config(image=photog,width="70",height="70")
    g.place(x=60,y=270)

    h=Button(root,justify = LEFT,command=play16)#button_16
    photoh=PhotoImage(file="num16.gif")
    h.config(image=photoh,width="70",height="70")
    h.place(x=170,y=270)

    i=Button(root,justify = LEFT,command=play17)#button_17
    photoi=PhotoImage(file="num17.gif")
    i.config(image=photoi,width="70",height="70")
    i.place(x=280,y=270)

    j=Button(root,justify = LEFT, command = btn_3, text ='Back')#button_main
    j.place(x=350,y=370)

    k=Button(root,justify = LEFT, command = btn_3_p, text ='<<')#button_nu_Ppage
    k.place(x=260,y=370)

    l=Button(root,justify = LEFT, command = btn_3_n, text ='>>')#button_nu_Npage
    l.place(x=300,y=370)
        
    root.mainloop()


'''----------------------------number page 3--------------------------------'''

def russian_nu3():
    def btn_3():
        root.destroy()
        russian()
    def btn_3_p():
        root.destroy()
        russian_nu2()
    def btn_3_n():
        root.destroy()
        russian_nu2()
    def play18():
        winsound.PlaySound('18-Audio Track.wav',1)
    def play19():
        winsound.PlaySound('19-Audio Track.wav',1)
    def play20():
        winsound.PlaySound('20-Audio Track.wav',1)
    def play30():
        winsound.PlaySound('30-Audio Track.wav',1)
    def play40():
        winsound.PlaySound('40-Audio Track.wav',1)
    def play50():
        winsound.PlaySound('50-Audio Track.wav',1)
    def play100():
        winsound.PlaySound('100-Audio Track.wav',1)
    def play500():
        winsound.PlaySound('500-Audio Track.wav',1)
    def play1000():
        winsound.PlaySound('1000-Audio Track.wav',1)
        
        
        
    root=Tk()

    root.geometry('420x420+200+200')#Menu Frame
    head = Label(root, text='เลข Russia',font='Courier 26')
    head.pack()

    a=Button(root,justify = LEFT,command=play18)#button_18
    photoa=PhotoImage(file="num18.gif")
    a.config(image=photoa,width="70",height="70")
    a.place(x=60,y=70)

    b=Button(root,justify = LEFT,command=play19)#button_19
    photob=PhotoImage(file="num19.gif")
    b.config(image=photob,width="70",height="70")
    b.place(x=170,y=70)

    c=Button(root,justify = LEFT,command=play20)#button_20
    photoc=PhotoImage(file="num20.gif")
    c.config(image=photoc,width="70",height="70")
    c.place(x=280,y=70)

    d=Button(root,justify = LEFT,command=play30)#button_30
    photod=PhotoImage(file="num30.gif")
    d.config(image=photod,width="70",height="70")
    d.place(x=60,y=170)

    e=Button(root,justify = LEFT,command=play40)#button_40
    photoe=PhotoImage(file="num40.gif")
    e.config(image=photoe,width="70",height="70")
    e.place(x=170,y=170)

    f=Button(root,justify = LEFT,command=play50)#button_50
    photof=PhotoImage(file="num50.gif")
    f.config(image=photof,width="70",height="70")
    f.place(x=280,y=170)

    g=Button(root,justify = LEFT,command=play100)#button_100
    photog=PhotoImage(file="num100.gif")
    g.config(image=photog,width="70",height="70")
    g.place(x=60,y=270)

    h=Button(root,justify = LEFT,command=play500)#button_500
    photoh=PhotoImage(file="num500.gif")
    h.config(image=photoh,width="70",height="70")
    h.place(x=170,y=270)

    i=Button(root,justify = LEFT,command=play1000)#button_1000
    photoi=PhotoImage(file="num1000.gif")
    i.config(image=photoi,width="70",height="70")
    i.place(x=280,y=270)

    j=Button(root,justify = LEFT, command = btn_3, text ='Back')#button_main
    j.place(x=350,y=370)

    k=Button(root,justify = LEFT, command = btn_3_p, text ='<<')#button_nu_Ppage
    k.place(x=260,y=370)

    l=Button(root,justify = LEFT, command = btn_3_n, text ='>>', state=DISABLED)#button_nu_Npage
    l.place(x=300,y=370)
        
    root.mainloop()




def russian_tb():
    def btn_3():
        root.destroy()
        russian()
        
    root=Tk()

    root.geometry('420x420+200+200')#Menu Frame
    head = Label(root, text='อักษร Russia',font='Courier 26')
    head.pack()



    b= Label(root,justify = LEFT)
    pic=PhotoImage(file='russianalfa-g.gif')
    b.config(image=pic,width="410",height="300")
    b.pack()
        


    a=Button(root,justify = LEFT, command = btn_3, text ='Back')#button_main
    a.place(x=350,y=370)
    root.mainloop()

'''------------------------------------history page-------------------------'''   
def history():
    def btn_2():
        root.destroy()
        main()
    def btn_2_n():
        root.destroy()
        history2()
    def btn_2_p():
        root.destroy()
        history()
    
    root=Tk()

    root.geometry('420x420+200+200')#Menu Frame
    head = Label(root, text='ประวัติ',font='Courier 26')
    head.pack()
    text = Label(root, text='ประวัติศาสตร์รัสเซีย เริ่มต้นขึ้นเมื่อชาวสลาฟตะวันออก',font='Courier 16').pack()
    text = Label(root, text='ก่อตั้งอาณาจักรคีวานรุส และรับเอาศาสนาคริสต์มาจาก',font='Courier 16').pack()
    text = Label(root, text='จักรวรรดิไบแซนไทน์ในปี พ.ศ.1531 ในปีพ.ศ.1783',font='Courier 16').pack()
    text = Label(root, text='อาณาจักรคีวานรุสล่มสลายโดยการรุกรานจากจักรวรรดิมองโกล',font='Courier 16').pack()
    text = Label(root, text='หลังจากคริสต์ศตวรรษที่ 13 มอสโกได้ค่อยพัฒนาเป็นศูนย์กลาง',font='Courier 16').pack()
    text = Label(root, text='ของศิลปะและวัฒนธรรมทีละน้อย ในคริสต์ศตวรรษที่ 15',font='Courier 16').pack()
    text = Label(root, text='รัฐมอสโกได้เป็นใหญ่ในจักรวรรดิรัสเซีย ซึ่งได้มีการขยายอาณาเขต',font='Courier 16').pack()
    text = Label(root, text='ถึงโปแลนด์ ทางด้านตะวันออกจรดมหาสมุทรแปซิฟิก',font='Courier 16').pack()
    text = Label(root, text='จนถึงสมัยพระเจ้าซาร์อีวานที่ 3 ในปี พ.ศ.2023',font='Courier 16').pack()
    text = Label(root, text='พระองค์หยุดส่งเครื่องบรรณาการให้มองโกเลีย',font='Courier 16').pack()
    text = Label(root, text='และประกาศเอกราชไม่เป็นเมืองขึ้นของมองโกเลียอีกต่อไป ',font='Courier 16').pack()

    a=Button(root,justify = LEFT, command = btn_2, text ='Back')#button_main
    a.place(x=350,y=370)

    b=Button(root,justify = LEFT, command = btn_2_p, text ='<<', state=DISABLED)#button_history_Ppage
    b.place(x=260,y=370)

    c=Button(root,justify = LEFT, command = btn_2_n, text ='>>')#button_history_Npage
    c.place(x=300,y=370)
    root.mainloop()
    
def history2():
    def btn_2():
        root.destroy()
        main()
    def btn_2_n():
        root.destroy()
        history3()
    def btn_2_p():
        root.destroy()
        history()

    
    root=Tk()

    root.geometry('420x420+200+200')#Menu Frame
    head = Label(root, text='ประวัติ2',font='Courier 26')
    head.pack()
    text = Label(root, text='หลังจากการเข้าร่วมในสงครามโลกครั้งที่หนึ่ง ส่งผลให้รัสเซีย',font='Courier 16').pack()
    text = Label(root, text='เผชิญปัญหาในการพัฒนาเป็นประเทศอุตสาหกรรม',font='Courier 16').pack()
    text = Label(root, text='ความเป็นอยู่ประชาชนลำบากแร้นแค้น กำลังทหารและ',font='Courier 16').pack()
    text = Label(root, text='เศรษฐกิจรัสเซียเข้าขั้นวิกฤต ในที่สุดพรรคคอมมิวนิสต์จึงได้',font='Courier 16').pack()
    text = Label(root, text='ก่อการปฏิวัติขึ้นในปี พ.ศ.2460 นำไปสู่การก่อตั้งสหภาพโซเวียต',font='Courier 16').pack()
    text = Label(root, text='เป็นประเทศแรกของโลกที่ปกครองด้วยระบอบคอมมิวนิสต์',font='Courier 16').pack()
    text = Label(root, text='หลังจากสงครามโลกครั้งที่สอง สหภาพโซเวียตกลายมาเป็น',font='Courier 16').pack()
    text = Label(root, text='ประเทศมหาอำนาจของโลกคู่กับสหรัฐอเมริกา ในช่วงสงครามเย็น',font='Courier 16').pack()
    text = Label(root, text='ในสมัยนั้น นโยบายของสหภาพโซเวียตได้เน้นการป้องกันประเทศ',font='Courier 16').pack()
    text = Label(root, text='และพัฒนาด้านอุตสาหกรรม แต่การเน้นพัฒนาทหารขนานใหญ่',font='Courier 16').pack()
    text = Label(root, text='ส่งผลทำให้เศรษฐกิจตกต่ำอย่างรุนแรง',font='Courier 16').pack()

    a=Button(root,justify = LEFT, command = btn_2, text ='Back')#button_main
    a.place(x=350,y=370)

    b=Button(root,justify = LEFT, command = btn_2_p, text ='<<')#button_history_Ppage
    b.place(x=260,y=370)

    c=Button(root,justify = LEFT, command = btn_2_n, text ='>>')#button_history_Npage
    c.place(x=300,y=370)
    root.mainloop()


def history3():
    def btn_2():
        root.destroy()
        main()
    def btn_2_n():
        root.destroy()
        history2()
    def btn_2_p():
        root.destroy()
        history2()

    
    root=Tk()

    root.geometry('420x420+200+200')#Menu Frame
    head = Label(root, text='ประวัติ3',font='Courier 26')
    head.pack()
    text = Label(root, text='ต่อมา เมื่อมิคาอิล กอร์บาชอฟ ขึ้นสู่อำนาจ',font='Courier 16').pack()
    text = Label(root, text='เขาได้เริ่มนโยบายปฏิรูปด้านต่าง ๆ',font='Courier 16').pack()
    text = Label(root, text='ทำให้สหภาพโซเวียตล่มสลายใน พ.ศ.2534 สาธารณรัฐต่าง ๆ',font='Courier 16').pack()
    text = Label(root, text='แยกตัวเป็นอิสระ สาธารณรัฐสังคมนิยมโซเวียตรัสเซีย',font='Courier 16').pack()
    text = Label(root, text='จึงแยกตัวออกมาเป็นเป็นสหพันธรัฐรัสเซียในปัจจุบัน',font='Courier 16').pack()
    text = Label(root, text='โดยที่รัสเซียได้รับสถานภาพตามกฎหมาย',font='Courier 16').pack()
    text = Label(root, text='ในเวทีระหว่างประเทศมาจากสหภาพโซเวียต',font='Courier 16').pack()

    a=Button(root,justify = LEFT, command = btn_2, text ='Back')#button_main
    a.place(x=350,y=370)

    b=Button(root,justify = LEFT, command = btn_2_p, text ='<<')#button_history_Ppage

    b.place(x=260,y=370)

    c=Button(root,justify = LEFT, command = btn_2_n, text ='>>', state=DISABLED)#button_history_Npage
    c.place(x=300,y=370)
    root.mainloop()


'''------------------------------------credit page-------------------------'''
def credit():
    def btn_3():
        root.destroy()
        main()
    root=Tk()

    root.geometry('420x420+200+200')#Menu Frame
    head = Label(root, text='Credit',font='Courier 26')
    head.pack()
    text = Label(root, text='',font='Courier 16').pack()
    text = Label(root, text='อ้างอิงจาก',font='Courier 18').pack()
    text = Label(root, text='Wikipedia',font='Courier 16').pack()
    text = Label(root, text='russianlessons.net',font='Courier 16').pack()
    text = Label(root, text='',font='Courier 16').pack()
    text = Label(root, text='จัดทำโดย',font='Courier 18').pack()
    text = Label(root, text='นายพีรณัฐ ฤกษ์ศุภสมพล 57070083',font='Courier 16').pack()
    text = Label(root, text='นายเมธิชัย อรัญชราธร 57070096',font='Courier 16').pack()
    
    c=Button(root,justify = LEFT, text ='Do not push me', state=DISABLED)#button_game
    c.place(x=250,y=370)
    a=Button(root,justify = LEFT, command = btn_3, text ='Back')#button_main
    a.place(x=350,y=370)

    root.mainloop()


main()


