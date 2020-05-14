# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:08:01 2020

@author: Naomi
"""

#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#Loop for 10 times
for i in range (0,11):
    #Define the basic variables of the model
    N=10000
    beta=0.3
    gamma=0.05
    #Create arrays for each of the variables
    I_list=[]
    S_list=[]
    R_list=[]
    #“infected” curves for 0, 10, 20, . . . 100 percent vaccination
    Vaccinated = i*0.1*N
    if Vaccinated == N:
        I = 0
        S = 0
    else:
        S = int(9999-Vaccinated)
        I = 1
    R = 0
    #Time=1000
    j=0
    while j<=1000:
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
        j+=1
    #Plot the results
    n = i * 10
    plt.plot(I_list, label=str(n)+'%',color=cm.viridis(i*35))
    plt.legend()
    plt.xlabel('time')
    plt.ylabel('number of people')
    plt.title('SIR model with different vaccination rates')
plt.show()
plt.savefig('SIR_vaccine',type='png')