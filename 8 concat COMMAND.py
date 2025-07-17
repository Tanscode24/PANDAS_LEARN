#CONCATINATING TWO DATAFRAMES TOGETHER
import pandas as pd
#DATASET 1
data1 = {
    'ID':[1,2,3,4,5],
    'NAME':['Amar','Bindu','Megha','Kittu','Ved'],
}
data2 = {
    'ID':[6,7,8,9],
    'NAME':['Mom','Bro','Sis','Chotu']
}
#DATAFRAME
df1= pd.DataFrame(data1)
df2= pd.DataFrame(data2)
#DISPLAY DATAFRAME
print("\nDATAFRAME 1 : \n",df1)
print("\nDATAFRAME 2 : \n",df2)
#CONCATINATING DATA1 AND DATA2
NewDf=pd.concat([df1,df2])
print("\n CONCATINATED DATA : \n",NewDf)
