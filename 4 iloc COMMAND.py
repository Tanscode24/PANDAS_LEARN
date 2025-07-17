#using DataFrame and accessing using row and columns using integer positions
import pandas as pd
dataset = {
    'student' : ['amar','tanu','ramu','raju','ravi'],
    'roll number' : [1,4,3,5,2],
    'marks ' : [100,50,80,30,20]
}

df = pd.DataFrame(dataset, index = ['RowA','RowB','RowC','RowD','RowE'])

print('STUDENT DETAILS : \n',df)

#ACCESSING DATA USING INTEGER POSITION BY USING iloc command

print ( '\nvalue : ',df.iloc[[1,2]])
