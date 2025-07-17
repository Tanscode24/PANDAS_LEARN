import numpy as np
import pandas as pd 
#DATASET 
data = [100,200,300,400,500,np.nan]
#CREATE SERIES 
s = pd.Series(data)
#DISPLAY THE DATA
print ( "SERIES : \n",s)
#ATTRIBUTES OF THE SERIES 
#--1-- DATATYPE OF THE SERIES : dtype 
print( "1.DATA TYPE OF THE SERIES : ", s.dtype)
#--2-- DIMENSION OF THE SERIES : ndim
print("2.DIMENSION OF THE SERIES : ",s.ndim)
#--3-- SIZE OF THE SERIES : size
print ( "3.SIZE OF THE SERIES : ", s.size)
#--4-- SETTING AND DISPLAYING THE NAME TO THE SERIES 
S = pd.Series(data, name = 'NUMBER SERIES')
print (S)
print ("4.NAME OF THE SERIES IS : ",S.name)
#--5-- DOES SERIES HAVE A nan (NOT A NUMBER) ATTRIBUTE 
#nan is a numpy attribute 
print ("5.DOES THE SERIES HAVE NAN : (TRUE/FLASE)",s.hasnans)
#--6-- INDEXING OF THE SERIES 
P = pd.Series(data, index = [1,2,3,4,5,6], name = 'SeriesWithIndex')
print ( "6.0.SERIES WITH INDEX : ",P)
print("6.1.INDEX OF THE SERIES : ",P.index)
#--7-- DISPLAY N-ROWS OF THE SERIES : head()
print("7.FIRST N-ROWS OF THE SERIES : ",s.head())
#--8-- DISPLAY THE N-LAST ROWS OF THE SERIES : tail()
print ("8.LAST N-ROWS OF THE SERIES : ",s.tail())
#--9-- DISPLAY THE INFORMATION ABOUT THE SERIES : info()
print ("9.INFORMATION ABOUT THE SERIES : ",P.info())



