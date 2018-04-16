# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 12:16:54 2018

@author: Administrator
"""

print('please input your Account(no more than 8 chars):')
account_1=input()     #get account that users input
print('please input your Password(no more than 8 chars):')
password_1=input()      #get password that users input
print('please make sure your Password(no more than 8 chars):')
password_temp=input()   #ensure the password that users input
while password_1!=password_temp:    #judge if the two password is the same
    print('please input again,you just input a different password:')
    password_temp=input()    #input the password aganin if the two password is different
else:
    print('you have registered successfully','\n','your account is:',account_1,'\n','your password is:',password_1)
print('please input the name of your hero')
heroName_1=input()    #get hero name that users input
print('please input the sex of your hero:1 for male, 2 for female ')
heroSex_1=input()    #get hero sex that users input
print('please input the type of your hero(1 for warrior,2 for wizard,3 for magician)')
heroType_1=input()    #get type of hero that users input
while heroSex_1!='1'and heroSex_1!='2':    #ensure the str that users input is '1' or '2'
    print('please input the sex of your hero again,make sure you input 1 for male or 2 for female!')
    heroSex_1=input()
if heroSex_1=='1':
    heroSex='male'
else:
    heroSex='female'
while heroType_1!='1'and heroType_1!='2'and heroType_1!='3':    #ensure the str that users input is '1' or '2' or '3' 
    print('please input the type of your hero again,make sure you input 1 for warrior or 2 for wizard or 3 for magician!')
    heroType_1=input()
if heroType_1=='1':
    heroType='warrior'
elif heroType_1=='2':
    heroType='wizard'
else:
    heroType='magician'
print('your hero has created successfully','\n','the name of your hero:',heroName_1,'\n','the sex of your hero:',heroSex,'\n','the type of your hero:',heroType,)    


      

