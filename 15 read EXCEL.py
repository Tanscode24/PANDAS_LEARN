import pandas as pd 

#INPUT EXCEL 
#LOAD AS DATAFRAME 
#READ EXCEL FILE : pandas.read_excel()
df = pd.read_excel(r'C:\\Users\\radhika singh\\OneDrive\Documents\\GitHub\\LEARN-PANDAS\DATASET\\cricket.xlsx')
print('EXCEL DATAFRAME : \n',df)

#DISPLAY FIRST n-ROWS IN THE DATAFRAME : pandas.head()
print('FIRST n-ROWS/5-ROWS IN THE EXCEL : \n',df.head())
print('FIRST 2-ROWS IN THE EXCEL : \n',df.head(2))

#DISPLAY LAST n-ROWS IN THE DATAFRAME : pandas.tail()
print ('LAST n-ROWS/5-ROWS IN THE EXCEL : \n',df.tail())
print ('LAST 3-ROWS IN THE EXCEL : \n',df.tail(3))