# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:02:33 2020

@author: Naomi
"""

seq ='ATGCGACTACGATCGAGGGCCAT'
#Define an empty string to store the complementary sequence
cDNA=""
#Loop through the sequence re
for i in seq:
    #if the character is 'A'
    if i=="A":
         #Store 'T' to the string cDNA
        cDNA+="T"
    #else if the character is 'T'  
    elif i=="T":
        #Store 'A' to the string cDNA
        cDNA+="A"
    #else if the character is 'C'
    elif i=="C":
        #Store 'G' to the string cDNA
        cDNA+="G"
    #else if the character is 'G'
    elif i=="G": 
         #Store 'C' to the string cDNA
        cDNA+="C"
#Reverse the complementary sequence
cDNA=cDNA[::-1]
#Print the reverse complementary sequence
print("The reverse complementary sequence:",cDNA)