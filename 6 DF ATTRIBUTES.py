#DataFrame Attributes in the pandas library
import pandas as pd
#DATASET
dataset = {
    'student':['tan','man','fan','can','ban'],
    'roll number':[1,2,3,4,5],
    'marks':[100,30,90,80,50]
}
#DATAFRAME
df=pd.DataFrame(dataset,index = [1001,1002,1003,1004,1005])

#DISPLAY
print("DATAFRAME : \n",df)

#DISPLAY THE DATATYPE : dtypes
print("\nDATA TYPES OF THE DATAFRAME IS  :\n",df.dtypes)

#DIMESNION OF THE DATAFRAME : ndim
print("\nDIMENSION OF THE DATAFRAME IS :\n",df.ndim)

#SIZE OF THE DATAFRAME : size
print("\nSIZE OF THE DATAFRAME IS : \n",df.size)

#DIMENSION OF THE MATRIX IN TUPLE FORM : shape
print("\n DIMENSIONS OF THE DATAFRAME :\n",df.shape)

#DISPLAY THE INDEXING OF THE DATAFRAME
print("\nINDEX :\n",df.index)

#TRANSPOSE OF THE DATAFRAME (MATRIX): TS
print("\nTRANSPOSE OF THE DATAFRAME :\n",df.T)

#DISPLAY FIRST n-ROWS : head()
print("\nFIRST n-ROWS OF THE DATAFRAME \n : ",df.head())
print("\nFIRST 2 ROWS OF THE DATAFRAME \n : ",df.head(2))

#DISPLAY LAST n-ROWS OF THE DATAFRAME : tail()
print("\n LAST n-ROWS : \n",df.tail())
print("\n LAST 3 ROWS : \n",df.tail(3))