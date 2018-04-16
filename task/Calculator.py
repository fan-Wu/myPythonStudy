# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 10:46:17 2018

@author: Administrator
"""

print ('please input the first number :')
firstNum= input()
firstNum=float(firstNum)
print ('the first number is :',firstNum,'and please input the second number :')
secondNum=input()
secondNum=float(secondNum)
print ('the second number is:',secondNum,'\n',)
print('and please choice your algorithms:','\n','"p" for plus;"ms" for minus;"mt"for multiplication;"d" for division')
algorithm_1=input()
if algorithm_1=='p' :
    print('the result is:',firstNum,'+',secondNum,'=',firstNum + secondNum)
elif algorithm_1=='ms' :
    print('the result is:',firstNum,'-',secondNum,'=',firstNum - secondNum)
elif algorithm_1=='mt' :
    print('the result is:',firstNum,'*',secondNum,'=',firstNum * secondNum) 
elif algorithm_1=='d' :
    print('the result is:',firstNum,'/',secondNum,'=',firstNum / secondNum)   
else:
    print('please input the right letter/letters for the right algorithms!')
    