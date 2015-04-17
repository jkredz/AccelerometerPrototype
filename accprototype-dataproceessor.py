## accprototype-dataprocessor.py		Justin Chin		16-April-2015
##
## Calculate function on data set for user selected time frame and function to handle the activity
## numpy functions can be applied to flatten the data and to handle determining activities during transitions during specified time windows
## numpy functions include (std,mean,min,mode)

import os, sys
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt            #converts csv into numpy arrays






def dataprocessor(tframe, funct, funct2):   #input the data, desired time interval, and the function you want to analyze with: (mean, std)
   line = filename.readline()                                                    #read first line of the file, which is the column header
   outfile.write(line)                                                           #write the header into the outputfile
   #outfile.write("\n")                                                           #write new line into outputfile
   tframe=int(tframe)                                                             #convert tframe from a string ipnut into an integer

   my_data = genfromtxt(sys.argv[1], delimiter=',')                               #converts source file data into a numpy array
   my_data=my_data[1:,:]                                                          #Reassign array to exclude first row of data since it is the header
   cols=my_data.shape[1]                                                          #Count the number of columns in the data set.  Sequence will be x,y,z with last column as activity indicator
   rows=my_data.shape[0]                                                          #Count rows of data

   if (rows%tframe != 0):                                                         #check if number of data rows is divisible by selected time frame
      my_data=my_data[rows%tframe:,:]                                             #if not, delete first few data series so rows%timeframe = 0
      rows=my_data.shape[0]                                                       #recalculate the number of rows in the array


   z= np.zeros([rows/tframe,cols],float)                                          #create empty array for flattened data
   for j in range(tframe,rows+1,tframe):                                          #j create row increments from tframe
      for i in range(cols-1):                                                     #i column increments from 0 to rows-1 (excluding the activity column)
         a=my_data[[range(j-tframe,j),i]]                                         #determine the rows and columns that will be calculated using the function
         b=getattr(a,funct)                                                       #set up the object "selected matrix" to be calculated by the function method
         result=b()                                                               #calculate the function on the selected time frame
         result=str(float(result))                                                #convert float result into string
         outfile.write(result)                                                    #write string into output file
         outfile.write(",")                                                       #write "," to create csv file
         z[(j/tframe)-1,i]=result                                                 #each calculated timeframe value is saved in the new condensed matrix Z

    #After going through each column, apply function2 to the activity column
      if (funct2 == 'mode'):
         a=my_data[[range(j-tframe,j),cols-1]]
         counts = np.bincount(a.astype(int))
         result = np.argmax(counts)
         result=str(float(result))
         outfile.write(result)
         z[(j/tframe)-1,cols-1]=result
         outfile.write("\n")
      else:
         a=my_data[[range(j-tframe,j),cols-1]]                                       #select timeframe data for the activity row
         b=getattr(a,funct2)                                                         #set up the object "selected matrix" to be calculated by the function2 method
         result=b()                                                                  #use function2 for the selected time frame of activity column
         result=str(float(result))
         outfile.write(result)
         z[(j/tframe)-1,cols-1]=result
         outfile.write("\n")
   print(z)


if __name__=='__main__':
   if len(sys.argv) != 6:
      print "USAGE:  python accprototpye-dataprocessor.py <input_filename> <time frame> <function> <function2> <output_filename>"
      sys.exit(1)

   # Open up the input and output files
   try:
      filename = open(sys.argv[1], 'r')
   except IOError:
      print "Could not open file '" + sys.argv[1] + "'.  Exiting."
      sys.exit(1)

   try:
      outfile = open(sys.argv[5], 'w')
   except IOError:
      print "Could not create file '" + sys.argv[5] + "'.  Exiting."
      infile.close()
      sys.exit(1)

   filename = open(sys.argv[1], 'r')
   tframe = sys.argv[2]
   funct = sys.argv[3]
   funct2 = sys.argv[4]

   dataprocessor(tframe, funct, funct2)
   filename.close()
   outfile.close()



