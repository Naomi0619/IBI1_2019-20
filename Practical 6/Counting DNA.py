# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 00:17:14 2020

@author: Naomi
"""

#Data to plot
a=int(input('A='))
b=int(input('G='))
c=int(input('C='))
d=int(input('T='))
import matplotlib.pyplot as plt
labels=['A','G','C','T']
count=[a,b,c,d]
colors=['lightsalmon','wheat','lightcyan','y']
#Plot
plt.pie(count, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False)
plt.title('pie of the four DNA nucleotides')
plt.axis('equal')
plt.show()