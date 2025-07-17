import pandas as pd 
#creating an array 
data=[100,200,300,400]
#CREATING A SERIES 
#ADDING INDEX 
s= pd.Series(data, index = ['RowA','RowB','RowC','RowD'])
print ('\nSeires of data : \n',s)
#ACCESSING THE SERIES VALUE USING : s[<INDEX>]
print("\nvalue at the 2nd index of the series : ",s[2])
#ACCESSING THE SERIES VALUE USING LABLES / INDEX WE HAVE GIVEN : S[<LABLE NAME>]
print('\n The value at the Row A index is : ', s['RowA'])
