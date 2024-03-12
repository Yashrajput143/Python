# -*- coding: utf-8 -*-
"""Statics2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z3BbH9OzHSM8vwsFiGA3TAFilPNeuSsV
"""

# Create series from array
import pandas as pd
df=pd.DataFrame()
print(df)

info={'ID':[101,102,103],'Department':['B.Sc','B.tech','M.tech']}
df=pd.DataFrame(info)
print(df)

info={'one':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f']),
      'two':pd.Series([1,2,3,4,5,6,7,8],index=['a','b','c','d','e','f','g','h'])}
d1=pd.DataFrame(info)
print(df)

info={'one':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f']),
      'two':pd.Series([1,2,3,4,5,6,7,8],index=['a','b','c','d','e','f','g','h'])}
d1=pd.DataFrame(info)
print(d1['one'])

info={'one':pd.Series([1,2,3,4,5],index=['a','b','c','d','e']),
      'two':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])}
df=pd.DataFrame(info)
# Add new column to an existing DataFrame object
print("Add new column by passing series")
df['three']=pd.Series([20,40,60],index=['a','b','c'])
print(df)
print("Add new column using existing DataFrame column")
df['four']=df['one']+df['three']
print(df)

# importing the pandas library
info={'one':pd.Series([1,2],index=['a','b']),
'two':pd.Series([1,2,3],index=['a','b','c'])}
df=pd.DataFrame(info)
print("The DataFrame:")
print(df)
#using del function
print("Delete the first column:")
del df['one']
print(df)
#using pop function
print("Delete the another column:")
df.pop('two')
print(df)

info={'one':pd.Series([1,2,3,4,5],index=['a','b','c','d','e']),
'two':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])}
df=pd.DataFrame(info)
print(df)

info={'one':pd.Series([1,2,3,4,5],index=['a','b','c','d','e']),
'two':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])}
df=pd.DataFrame(info)
print(df.iloc[3])

info={'one':pd.Series([1,2,3,4,5],index=['a','b','c','d','e']),
'two':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])}
df=pd.DataFrame(info)
print(df.iloc[2:5])

d=pd.DataFrame([[7,8],[9,10]],columns=['x','y'])
d2=pd.DataFrame([[11,12],[13,14]],columns=['x','y'])
d=d.append(d2)
print(d)

a_info=pd.DataFrame([[4,5],[6,7]],columns=['x','y'])
b_info=pd.DataFrame([[8,9],[10,11]],columns=['x','y'])
a_info=a_info.append(b_info)
#drop rows with label 0
a_info=a_info.drop(0)