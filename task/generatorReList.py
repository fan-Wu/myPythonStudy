# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 08:26:03 2018

@author: Administrator
"""

class MyList:
    __list=[]
    def __init__(self,*args):
        for arg in args:
            self.__list.append(arg)

    def __add__(self,x):
        self.__list=(i+x for i in self.__list)
        return self.__list
            
    def __sub__(self,x):
        self.__list=(i-x for i in self.__list)
        return self.__list
    
    def __mul__(self,x):
        self.__list=(i*x for i in self.__list)
        return self.__list
    
    def show(self):
        for n in self.__list:
            print (n)

if __name__ =='__main__':
    l=MyList(1,2,3,4,5,6,7)
    l+5
    l*5
    l-5
    l.show()