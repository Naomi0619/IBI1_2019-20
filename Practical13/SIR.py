# -*- coding: utf-8 -*-
"""
Created on Thu May 14 14:15:29 2020

@author: Naomi
"""

#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#Define the basic variables of the model
N=10000
S=9999
I=1
R=0
beta=0.3
gamma=0.05
#Create arrays for each of the variables
I_list=[]
S_list=[]
R_list=[]
#Time=1000 
for i in range (0,1001):
    #Compute the probability of infection
    I_probability=beta*(I/N)
    #Susceptible - Infected - Recovered
    I0=sum(np.random.choice(range(2),S,p=[1-I_probability,I_probability]))
    R0=sum(np.random.choice(range(2),I,p=[1-gamma,gamma]))
    S=S-I0
    I=I+I0-R0
    R=R+R0
    #New arrays for each of the variables
    I_list.append(I)
    S_list.append(S)
    R_list.append(R)
#Plot the results
plt.figure(figsize=(6, 4),dpi=150)
plt.plot(S_list , label='susceptible')
plt.plot(I_list, label='infected')
plt.plot(R_list, label='recovered')
plt.legend()
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.show()
plt.savefig('SIR',type='png')