#JOINING DATAFRAMES
import pandas as pd
#DATASET 1
data1 = {
    'Name':['Ram','Sham','Lakshman','Rita','Sohan'],
    'Roll Number':[1,2,3,4,5]
}
data2 = {
    'Marks':[100,30,40,50,60],
    'Grade':['A+','C','C+','B','B+']
}
#DATAFRAMES
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
#DISPLAY DATAFRAMES
print("DATASET 1 : \n",df1)
print("DATASET 2 : \n",df2)
#JOINGING TWO DATAFRAMES TOGETHER
newdf = df1.join(df2)
print("JOINED DATAFRAME : \n",newdf)