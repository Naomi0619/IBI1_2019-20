# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 03:08:02 2020

@author: Naomi
"""

#Define a function
def power(x):
    v=[]
    print('%d is 2**'%x,end='')
    while (x>0):
        v.append(int(x%2))
        x=int(x/2)
    for i in range(0,len(v)):
        if(v[i]==1):
            print(i,end='')
            if(i!=len(v)-1):
                print('+2**', end='')
    print('\n')
#Start
print('Set a number: ')
x=int(input('x='))
x=power(x)