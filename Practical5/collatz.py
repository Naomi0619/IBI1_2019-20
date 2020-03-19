# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 19:40:03 2020

@author: Naomi
"""
#Define the function
def collatz(number):
    if number%2==0:
        number=number/2
        print(number//2)
    else:
        number=3*number+1
    print(number)
    return number
#Start
print ('Collatz sequence:')
try:
    number=int(input('n='))
    while number!=1:
          number=collatz(number)
          continue
except:
         print('Error')