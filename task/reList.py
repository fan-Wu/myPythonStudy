# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 21:26:43 2018
重写列表类，重载运算符
@author: Administrator
"""
class MyList:
    __list=[]
    def __init__(self,*args):
        for arg in args:
            self.__list.append(arg)
    def __add__(self,x):
        for i in range(0,len(self.__list)):
            self.__list[i]= self.__list[i]+x
        return self.__list
            
    def __sub__(self,x):
        for i in range(0,len(self.__list)):
            self.__list[i]= self.__list[i]-x
        return self.__list
    
    def __mul__(self,x):
        for i in range(0,len(self.__list)):
            self.__list[i]= self.__list[i]*x
        return self.__list
    
    def show(self):
        print(self.__list)

if __name__ =='__main__':
    l=MyList(1,2,3,4,5,6)
    l+5
    l.show()
    l*5
    l.show()
    l-5
    l.show()
    
