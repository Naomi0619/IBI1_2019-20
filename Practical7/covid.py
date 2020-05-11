# -*- coding: utf-8 -*-
"""
Created on Sun May 10 14:46:44 2020

@author: Naomi
"""

#Import some python libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Change the working directory to where your full_data.csv file is stored
os.chdir('C:/Users/Naomi/Desktop/IBI/Practical/7 Working with Global Health Data')
#Read the content of the full_data.csv into a dataframe object
covid_data = pd.read_csv("full_data.csv")

#Show all columns and every third row between (and including) 0 and 15
print('All columns and every third row between (and including) 0 and 15:\n ', covid_data.iloc[0:16:3,:])

#Read  the “location” column and all the rows
location=covid_data.loc[:,'location']
#Create a Boolean that is True when the “location” is “Afghanistan”
my_rows1=[]
for i in location:
    if i=='Afghanistan':
        my_rows1.append(True)
    else:
        my_rows1.append(False)
#Show every row where the location is “Afghanistan”
print('\n“total cases” for all rows corresponding to Afghanistan:\n', covid_data.loc[my_rows1,'total_cases'])

#Create a Boolean that is True when the “location” is “World”
my_rows2=[]
for i in location:
    if i=='World':
        my_rows2.append(True)
    else:
        my_rows2.append(False)
#Store the data on new cases for the entire world
world_new_cases=covid_data.loc[my_rows2,'new_cases']
#Compute the mean for new cases around the world
print('\nThe mean for new cases around the world:',np.mean(world_new_cases))
#Compute the median for new cases around the world
print('The median for new cases around the world:',np.median(world_new_cases))

#Create a boxplot of new cases worldwide
plt.boxplot(world_new_cases, showmeans=True, labels=' ')
#The title of the boxplot
plt.title('New Cases Worldwide')
#The axis label
plt.ylabel('Number')

#Store the data on dates for the entire world
date=covid_data.loc[:, 'date']
world_dates=covid_data.loc[my_rows2, 'date']
#Store the data on new deaths for the entire world
new_deaths=covid_data.loc[:, 'new_deaths']
world_new_deaths=covid_data.loc[my_rows2, 'new_deaths']
#Plot both new cases and new deaths worldwide
plt.figure()
plt.plot(world_dates, world_new_cases, 'r.', label='new cases')
plt.xticks(world_dates.iloc[0:len(world_dates):4], rotation=-90)
plt.plot(world_dates, world_new_deaths,'b.', label='new deaths')
#Title
plt.title('New Cases and New Deaths Worldwide')
#Legend
plt.legend()
#Axis labels
plt.xlabel('Date') 
plt.ylabel('Number')

#Create a Boolean that is True when the “location” is “Spain”
my_rows3=[]
for i in location:
    if i=='Spain':
        my_rows3.append(True)
    else:
        my_rows3.append(False)
#Store the data on new cases for Spain
Spain_new_cases=covid_data.loc[my_rows3,'new_cases']
#Store the data on total cases for Spain
Spain_total_cases=covid_data.loc[my_rows3,'total_cases']
#Store the data on dates for Spain
Spain_dates=covid_data.loc[my_rows3,'date']
#Plot both new cases and total cases in Spain
plt.figure()
plt.plot(Spain_dates, Spain_new_cases, 'y.', label='new cases')
plt.xticks(world_dates.iloc[0:len(world_dates):4], rotation=-90)
plt.plot(Spain_dates, Spain_total_cases,'c.', label='total cases')
#Title
plt.title('New Cases and Total Cases in Spain over Time')
#Legend
plt.legend()
#Axis labels
plt.xlabel('Date') 
plt.ylabel('Number')