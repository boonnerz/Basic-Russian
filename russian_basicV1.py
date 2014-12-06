#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *

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

    a=Button(root,justify = LEFT,command = btn1)#button_russ
    photoa=PhotoImage(file="ruski-g.gif")
    a.config(image=photoa,width="110",height="110")
    a.place(x=65,y=100)

    b=Button(root,justify = LEFT,command = btn2)#button_know
    photob=PhotoImage(file="common-g.gif")
    b.config(image=photob,width="110",height="110")
    b.place(x=245,y=100)

    c=Button(root,justify = LEFT,command = btn3)#button_us
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
    root=Tk()

    root.geometry('420x420+200+200')#Menu Frame
    head = Label(root, text='Basic Words!',font='Courier 26')
    head.place(x=70,y=30)

    a=Button(root,justify = LEFT, command = btn_1, text ='Back')#button_russ
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

    a=Button(root,justify = LEFT, command = btn_2, text ='Back')#button_russ
    a.place(x=350,y=370)

    b=Button(root,justify = LEFT, command = btn_2_p, text ='<<', state=DISABLED)#button_russ
    b.place(x=260,y=370)

    c=Button(root,justify = LEFT, command = btn_2_n, text ='>>')#button_russ
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

    a=Button(root,justify = LEFT, command = btn_2, text ='Back')#button_russ
    a.place(x=350,y=370)

    b=Button(root,justify = LEFT, command = btn_2_p, text ='<<')#button_russ
    b.place(x=260,y=370)

    c=Button(root,justify = LEFT, command = btn_2_n, text ='>>')#button_russ
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

    a=Button(root,justify = LEFT, command = btn_2, text ='Back')#button_russ
    a.place(x=350,y=370)

    b=Button(root,justify = LEFT, command = btn_2_p, text ='<<')#button_russ
    b.place(x=260,y=370)

    c=Button(root,justify = LEFT, command = btn_2_n, text ='>>', state=DISABLED)#button_russ
    c.place(x=300,y=370)
    root.mainloop()


'''------------------------------------credit page-------------------------'''
def credit():
    def btn_3():
        root.destroy()
        main()
    root=Tk()
    #def game():    latre

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
    
    c=Button(root,justify = LEFT, text ='Mini game', state=DISABLED)#button_game
    c.place(x=250,y=370)
    a=Button(root,justify = LEFT, command = btn_3, text ='Back')#button_back
    a.place(x=350,y=370)

    root.mainloop()



main()


