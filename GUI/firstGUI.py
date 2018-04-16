# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 13:32:41 2018

@author: Administrator
"""

import tkinter
import turtle
tk1=tkinter.Tk()

def draw(event):
    for i in range(5):
        turtle.fd(200)
        turtle.rt(144)
        

label=tkinter.Label(tk1,text='你好')
label.pack()
button1=tkinter.Button(tk1,text='五角星')
button1.pack()
button1.bind('<Button-1>',draw)

M=tkinter.Menu(tk1)
subM=tkinter.Menu(M,tearoff=0)
subM.add_command(label='open')
subM.add_command(label='save')
subM.add_command(label='exit')
M.add_cascade(label='File',menu=subM)
tk1.config(menu=M)
 
tk1.mainloop()