# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 20:56:33 2018
frame TextCtr Button StaticText Bind Sizer  flag proportion ..
@author: Administrator
"""

import wx
import time

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title="Xini's chatting room",size=(520,450))
        panel=wx.Panel(self)
        labelAll=wx.StaticText(panel,-1,'History message')
        self.textAll=wx.TextCtrl(panel,-1,
                                 size=(480,200),
                                 style=wx.TE_MULTILINE|wx.TE_READONLY)
        
        labelIn=wx.StaticText(panel,-1,'Message')
        self.textIn=wx.TextCtrl(panel,-1,
                                 size=(480,100),
                                 style=wx.TE_MULTILINE)
        
        self.btnSent=wx.Button(panel,-1,'sent',size=(75,25))
                              
        self.btnClear=wx.Button(panel,-1,'clear',size=(75,25))
        
        self.Bind(wx.EVT_BUTTON,self.OnButtonSent,self.btnSent)
        self.Bind(wx.EVT_BUTTON,self.OnButtonClear,self.btnClear)

        btnSizer=wx.BoxSizer()
        btnSizer.Add(self.btnSent,proportion=0)
        btnSizer.Add(self.btnClear,proportion=0)

        mainSizer=wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(labelAll,proportion=0,flag=wx.ALIGN_CENTER)
        mainSizer.Add(self.textAll,proportion=1,flag=wx.EXPAND)
        mainSizer.Add(labelIn,proportion=0,flag=wx.ALIGN_CENTER)
        mainSizer.Add(self.textIn,proportion=0,flag=wx.EXPAND)
        mainSizer.Add(btnSizer,proportion=0,flag=wx.ALIGN_CENTER)

        panel.SetSizer(mainSizer)
        
        
    def OnButtonSent(self,event):
        userInput=self.textIn.GetValue()
        now=time.ctime()
        self.textIn.Clear()
        msgInput="You(%s):\n %s \n"%(now,userInput)
        self.textAll.AppendText(msgInput)
    
    def OnButtonClear(self,event):
        self.textIn.Clear()
    
app=wx.App()
frame=MyFrame()
frame.Show()
app.MainLoop()
