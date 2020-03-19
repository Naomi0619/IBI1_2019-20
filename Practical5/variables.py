# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 17:40:07 2020

@author: Naomi
"""

#Some simple math
a=123
b=123123
print(b%7)
c=b/7
d=b/11
e=b/13

#Booleans
import random
list=[True,False]
X=random.choice(list)
Y=not X
Z=(X and not Y) or (Y and not X)
W=(X!=Y)
print(Z)
print(W)
print(Z==W)