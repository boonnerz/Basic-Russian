#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk

root = tk.Tk()

word = tk.Label(root, text="สวัสดี Tkinter!")
word.pack()

def callback():
    """change text of Label => word"""
    word.config(text="เปลี่ยน!")

btn_changeword = tk.Button(root, text="เปลี่ยนคำ", command=callback)
btn_changeword.pack()

tk.mainloop()
