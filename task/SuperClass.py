# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 09:20:01 2018
surper 经典类 新式类
@author: Administrator
"""

class A:
    def __init__(self):
        print('enter A')
        print('leave A')

class B(A):
    def __init__(self):
        print('enter B')
        A.__init__(self)
        print('leave B')

class C(A):
    def __init__(self):
        print('enter c')
        A.__init__(self)
        print('leave c')

class D(B,C):
    def __init__(self):
        print('enter D')
        B.__init__(self)
        C.__init__(self)
        print('leave D')

d=D()

'''***************************'''
print('-'*50)
class A:
    def __init__(self):
        print('enter A')
        print('leave A')

class B(A):
    def __init__(self):
        print('enter B')
        super(B,self).__init__()
        print('leave B')

class C(A):
    def __init__(self):
        print('enter c')
        super(C,self).__init__()
        print('leave c')

class D(B,C):
    def __init__(self):
        print('enter D')
        super(D,self).__init__()
        print('leave D')

d=D()
