# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:36:10 2020

@author: Naomi
"""

#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#Make array of all susceptible population
population=np.zeros((100,100))
#Randomly select the x and y coordinates of where the outbreak is happening and store it.
outbreak=np.random.choice(range(100),2)
#Address the person with those exact coordinates in our population array and change their status from 0 (susceptible) to 1 (infected).
population[outbreak[0],outbreak[1]]=1
#Create the first figure
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
#Set up the model parameters
beta=0.3
gamma=0.05
#Loop for 100 times
for i in range (0,101):
    #Find infected points
    infectedIndex = np.where(population==1)
    #Loop through all infected points
    for j in range(len(infectedIndex[0])):
        #Get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        #Infect each neighbour with probability beta
        #Infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                if (xNeighbour,yNeighbour) != (x,y):
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        #Only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
        population[x,y]=np.random.choice(range(1,3),1,p=[1-gamma,gamma])[0]
    #Plot the ooutcomes
    time=[0,10,50,100]
    if i in time:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title('Spacial_SIR'+str(i))
            