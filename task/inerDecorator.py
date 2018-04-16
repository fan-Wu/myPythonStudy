# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 09:30:21 2018
内置装饰器、类静态方法、类方法、属性方法(staticmethod,classmethod,property)
@author: Administrator
"""

class Human:
    __money=10000
    age=25
    
    @property
    def howOld(self):
        return self.age
    
    def earn(self,x):
        self.__money= self.__money+x
    
    @classmethod
    def purchase(self,x):
        self.__money= self.__money-x
    
    @staticmethod   #类静态方法 不设定self使得对象可以调用此方法
    def say():
        print (' sorry i cant')
    
    def money(self):
        print (self.__money)
   
h=Human()
h.say()
Human.purchase(1000)
print(h.howOld)
h.money()