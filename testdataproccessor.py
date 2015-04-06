__author__ = 'justin'
import numpy as np
import matplotlib.pyplot as plt
import random
from numpy import matrix


funct=['std','mean','sum']

SPN = np.random.randint(0,100,[100,10])
print(SPN)

tframe=10                                          #set time intervals

col=SPN.shape[1]
row=SPN.shape[0]

z= np.zeros([row/tframe,col],float)

#print(SPN[[0,1,2,3,4,5,6,7,8,9],0].sum())
#print(SPN[[10,11,12,13,14,15,16,17,18,19],0].sum())
#print(SPN[[20,21,22,23,24,25,26,27,28,29],0].sum())
#print(SPN[[30,31,32,33,34,35,36,37,38,39],0].sum())
l='sum'                                             #select function

for j in range(tframe,row+1,tframe):                #iterate each row by intervals of selected timeframe
      for i in range(col):                          #iterate through each column
         a=SPN[[range(j-tframe,j),i]]               #determine the rows and columns that will be calculated using the function
         b=getattr(a,l)                             #set up the object "selected matrix" to be calculated by the function method
         result=b()
         #print(a)
         #print(i)
         #print(range(j-tframe,j))
         z[(j/tframe)-1,i]=result                      #each calculated timeframe value is saved in the new condensed matrix

print(z)

"""
print(function[2])
k=function[2]


d=matrix([[1,1,1],
   [1,1,1],
   [1,1,1]])
print(d)
print(d.sum())
try:
    k=getattr(d,k)
except AttributeError:
    print("error")
else:
    result=k()
    print(result)
"""