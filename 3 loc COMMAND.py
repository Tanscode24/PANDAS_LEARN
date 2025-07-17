#Access group of rows and columns in the pandas dataframe
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

#dataset
data = {
    "student" : ["tanihska singh","rahul sharma","mayank singhal","anand bush"],
    "roll no" : [1,2,3,4],
    "marks" : [100,30,50,60]
}

df = pd.DataFrame(data,index = ['RowA','RowB','RowC','RowD'],)
print ( "here is the student detail below : \n\n", df)

#ACCESSING THE VALUES OF THE DATASET IN COLUMN

print( "\n value : ", df.loc['RowA','student'])


