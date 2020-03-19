# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 01:26:10 2020

@author: Naomi
"""
#filtering
data=list(map(int,input('gene_lengths=').split()))
data.remove(max(data))
data.remove(min(data))
print(data)
#Draw a boxplot
import matplotlib.pyplot as plt
plt.boxplot(x=data, labels=[''],showmeans=True)
plt.title('gene lengths')
plt.show()