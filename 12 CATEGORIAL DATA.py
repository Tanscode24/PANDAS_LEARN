import pandas as pd

#--1-- CREATING CATEGORIAL SERIES IN THE PANDAS 
#DATASET
data = ['A','B','C','D','C']
#USING dtype METHOD
s = pd.Series(data,dtype='category')
print ("CATEGORIAL SERIES : \n",s)

#--2-- CREATING CAEGORIAL DATAFRAME IN THE PANDAS 
df = pd.DataFrame({'CAT1' :list('pqrs'), 'CAT2': list('pqqr'),'CAT3' : list('prss') },dtype='category')
print ("DATAFRAME : \n",df)
#DISPLAYING THE DATATYPE OF THE DATAFRAME 
print ( "DATATYPE OF EACH COLUMN IN THE DATAFRAME : \n",df.dtypes)
