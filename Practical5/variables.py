# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 17:40:07 2020

@author: Naomi
"""

#Some simple math

#Store a 3-digit number in a
a=123
#Write the digits of a twice
b=123123
#Check whether b can be divided by 7
if b%7==0:
    print('b can be divided by 7')
else:
    print('b cannot be divided by 7')
#Assign c to be b divided by 7
c=b/7
#Assign d to be c divided by 11
d=c/11
#Assign e to be c divided by 13
e=d/13
#Compare e to a
if e>a:
    print('e is greater than a')
elif e<a:
    print('a is greater than e')
else:
    print('a is equal to e')


#Booleans

#Make X=True or False
import random
list=[True,False]
X=random.choice(list)
#Make X and Y opposite
Y=not X
#Define Z and W
Z=(X and not Y) or (Y and not X)
W=(X!=Y)
#Verify that Z is always true
print('Z is always',Z)
#Verify that Z and W are always the same
if Z==W:
    print('Z and W are always the same.')
else:
    print('Z are not always the same as W.')
