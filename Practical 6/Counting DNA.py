# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 00:17:14 2020

@author: Naomi
"""

#Import the number of four nucleotides
a=int(input('A='))
b=int(input('G='))
c=int(input('C='))
d=int(input('T='))
#Count the frequency table
s={'A':"%1.1f%%"%(a/21*100),'G':"%1.1f%%"%(b/21*100),'C':"%1.1f%%"%(c/21*100),'T':"%1.1f%%"%(d/21*100)}
#Print the frequency table
print('The frequency table:',s)
#Import matplotlib
import matplotlib.pyplot as plt
#Labels of the pie
labels=['A','G','C','T']
#Data for the pie
count=[a,b,c,d]
#Colors of the pie
colors=['lightsalmon','wheat','lightcyan','y']
#Plot the pie
plt.pie(count, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False)
#Title of the pie
plt.title('pie of the four DNA nucleotides')
#Make the pie circular
plt.axis('equal')
#Print the pie
plt.show()