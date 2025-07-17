import pandas as pd 
#DATASET 1
data1 = [100,200,300,400,500]
#DATASET 2 
data2 = [60,700,80,900,100]
#FORMING THE SERIES : pandas.Series(DATASET)
s1 = pd.Series(data1)
s2 = pd.Series(data2)
#DISPLAY THE SERIES 
print ("SERIES 1 : \n",s1)
print ("SERIES 2 : \n",s2)
#COMBINIGN THESE SERIES : SERIES1.combine(SERIES2,FUNCTION)

#CREATING THE FUNCTION FOR COMPARING THE TWO SERIES 
def max(x1,x2):
    if(x1>x2):
        return x1
    else:
        return x2

maxS = s1.combine(s2,max)
print ("MAX ELEMENT COMBINED SERIES : \n",maxS)

def min(x1,x2):
    if (x1<x2):
        return x1
    else:
        return x2

minS=s1.combine(s2,min)
print ('MIN ELEMENT COMBINED SERIES : \n',minS)