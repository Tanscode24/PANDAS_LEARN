import pandas as pd 
#INPUT CSV 
#LOADING CSV IN A DATAFRAME 
#READING A CSV FILE : pandas.read_csv() 

df = pd.read_csv(r'C:\Users\radhika singh\OneDrive\Documents\GitHub\LEARN-PANDAS\DATASET\students.csv')
print ('OUR DATAFRAME : \n',df)

#DISPLAY FIRST n-ROWS FROM THE DATAFRAME : head()
print ('FRIST n-ROWS : \n',df.head())
print ('FIRST 2-ROWS : \n',df.head(2))

#DISPLAY LAST n-ROWS FROM THE DATASET : tail()
print('LAST n-ROWS : \n',df.tail())
print ('LAST 3-ROWS : \n',df.tail(3))