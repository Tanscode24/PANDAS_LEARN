#dataframes in pandas
import pandas as pd
#dataset
data = {
    "student" : ["rohit","rishi","saurabh","aashi","manay"],
    "roll no" : [1,2,3,4,5],
    "marks" : [20,30,20,40,50]
}

df = pd.DataFrame(data)

print( "student information\n\n",df)

