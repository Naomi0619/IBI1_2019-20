# -*- coding: utf-8 -*-
"""
Created on Fri May 15 01:53:44 2020

@author: Naomi
"""

#Import necessary libraries
import pandas as pd
import xml.dom.minidom as xdm
#GO id
ID=[]
#Term name
name=[]
#Definition string
definition=[]
#Number of child nodes
childnodes=[]
#Read the xml file
gotree=xdm.parse('C:/Users/Naomi/Desktop/IBI/Practical/14 Practical Manipulating XML files/go_obo.xml')
go=gotree.documentElement
#Find the number of childNodes for each 'autophagosome' related gene ontology term
def childNodes(n1):
    global terms
    childnodes=0
    #Find 'is_a'
    for term in terms:
        is_a=term.getElementsByTagName('is_a')
        for parent in is_a:
            #If n1 is parent
            if parent.childNodes[0].data==n1:
                childnodes+=1
                #Count childnodes
                n2=term.getElementsByTagName('id')[0].childNodes[0].data
                childnodes+=childNodes(n2)
    return childnodes
#Find terms
terms=go.getElementsByTagName('term')
#Find contents in <defstr>
for term in terms:
    d=term.getElementsByTagName('def')[0]
    defstr=d.getElementsByTagName('defstr')[0].childNodes[0].data
    #If 'autophagosome' is found
    if defstr.find('autophagosome')>-1 or defstr.find('Autophagosome')>-1:
        #Extract id, name and definition
        n1=term.getElementsByTagName('id')[0].childNodes[0].data
        ID.append(n1)
        name.append(term.getElementsByTagName('name')[0].childNodes[0].data)
        definition.append(defstr)
        #The number of childnodes
        childnodes.append(childNodes(n1))
#Save data in the excel file
data={'id':ID,'name':name,'definition':definition,'childnodes':childnodes}
dataframe=pd.DataFrame(data)
dataframe.to_excel(r'C:/Users/Naomi/Desktop/IBI/Practical/IBI1_2019-20/Practical14/autophagosome.xlsx')