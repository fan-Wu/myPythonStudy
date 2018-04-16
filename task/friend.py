# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 16:34:23 2018

@author: Administrator
"""

strThatInput=input('please input a str :')
letterCount=[0,0,0,0,0,0]
i=0
f='friend'
while i<len(strThatInput):
    if f.find(strThatInput[i])==-1:
        i+=1
    else:
        letterCount[f.find(strThatInput[i])]+=1
        i+=1
print (letterCount)