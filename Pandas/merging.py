import numpy as np
import pandas as pd

df1 = pd.DataFrame({
    'ID':[22,43],
    'Name': ['Utsav', 'Peter']
})
df2 = pd.DataFrame({
    'ID' : [22,43],
    'Age': [21,19]
})

merged = pd.merge(df1,df2,on='ID')
print(merged)
