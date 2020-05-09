# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 01:26:10 2020

@author: Naomi
"""
#Import the ten gene lengths to the list
data=list(map(int,input('gene_lengths=').split()))
#Sort the list
data.sort()
#Remove the maximum and minimum
data.remove(max(data))
data.remove(min(data))
#Print the list
print('List of sorted values without the most value:',data)
#Import the matplotlib
import matplotlib.pyplot as plt
#Draw the boxplot
plt.boxplot(x=data, labels=[''],showmeans=True)
#Title of the boxplot
plt.title('gene lengths')
#Print the boxplot
plt.show()