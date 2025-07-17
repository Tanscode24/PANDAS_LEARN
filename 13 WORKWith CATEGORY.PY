import pandas as pd 
#CREATING CATEGORIAL SERIES 
s = pd.Series(data=['p','q','r','s'], dtype = 'category')
print ('ACTUAL CATEGORIAL SERIES : \n',s)
#APPENDING NEW CATEGORY IN THE SERIES 
S = s.cat.add_categories('t')
print ('APPENDED CATEGORIAL SERIES : \n',S)

#REMOVING CATEGORY 
R = S.cat.remove_categories('p')
print ('REMOVED CATEGORY : /n',R)