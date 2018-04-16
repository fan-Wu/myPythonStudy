# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 08:17:22 2018

@author: Administrator
"""
'''
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and i!=k and j!=k:
                print ("%d%d%d"%(i,j,k)) '''
import time
import math

def BQBJ():
    x=1
    y=1
    start=time.clock()
    while x <20:
       while y<33:
           z=100-x-y
           if z%3==0 and 5*x+3*y+z/3==100:
               print('x=%d,y=%d,z=%d'%(x,y,z))
               break
           else:
               y+=1
       y=1
       x+=1
    end=time.clock()
    T=(end-start)/1000    
    print(T)

def TEST2():
    for a in range(0,68):
        if math.sqrt(a*a+168)%1==0:
            print(a*a-100)
            


TEST2()
