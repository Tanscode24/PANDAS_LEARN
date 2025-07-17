#iterating the DataFrame using for loop
import pandas as pd
dataset = {
    'student ' : ['roma','raj','rahul','rashmi','lokesh'],
    'roll number ' : [1,2,3,4,5],
    'marks ' : [100,20,40,50,60]
}
#DataFrame is used to assign the data to a variable so that i can be printed in a tabular form
df = pd.DataFrame(dataset)
#index argument is used to assign the names to the index as per your choice and convenience
df = pd.DataFrame(dataset, index = ['student 1','student 2','student 3','student 4','student 5'])
print ('STUDENT DETAILS ARE AS FOLLOW : \n',df)

#iterating the columns of the dataset using for loop
print("\n displaying the column of the dataframe : \n")
for col in df :
    print(col)
