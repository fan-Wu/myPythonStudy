# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 15:23:57 2018

@author: Administrator
"""
import wx

class App(wx.App):
    def OnInit(self):
        image=wx.Image('wxPython.jpg',wx.BITMAP_TYPE_JPEG)
        self.frame=Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

class Frame(wx.Frame):
    def __init__(self,image,parent=None,id=-1,
                 pos=wx.DefaultPosition,
                 title='Xini'):
        temp=image.ConvertToBitmap()
        size=temp.GetWidth(),temp.GetHeight()
        wx.Frame.__init__(self,parent,id,title,pos,size)
        self.bmp=wx.StaticBitmap(parent=self,bitmap=temp)


def main():
    app=App()
    app.MainLoop()
