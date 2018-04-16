# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 17:54:42 2018

@author: Administrator
"""

initialNum=int(input('please input your initial number:'))
print (initialNum)
while initialNum>1:
    if initialNum%2==0:
        initialNum /=2
        print (initialNum)
    if initialNum%2==1 and initialNum!=1:
        initialNum=initialNum*3+1
        print (initialNum)