# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 20:51:43 2018
面向对象：类、对象、多态、继承。。
@author: Administrator
"""

class father:
    '''this is class father'''
    def __init__(self,money,__money):
        self.money=money
        self.__money=__money
    def drive(self):
        '''this is method drive'''
        print('i can drive a car')
    def __str__(self):
        msg='this is __str__'
        return msg
        
class mother:
    def __init__(self,mymoney):
        self.mymoney=mymoney 
    def drive(self,carType):
        print('i can drive a %s'%carType)

class son(father):
    def drive(self,carType):
          print('i can drive a %s'%carType)

s=son(1,2)
s.drive('tank')
