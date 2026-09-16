import numpy as np
import pandas as pd

data = {
    "A" : [1,2, np.nan,4,5],
    "B" : [np.nan,2,3,4,5],
    "C" : [1,2,3, np.nan,np.nan],
    "D": [1,np.nan,np.nan, np.nan,5]
}

df = pd.DataFrame(data)
print(df)
print(df.isna())
print(df.isna().sum())

#Check is there any Missing value in Data???

print(df.isna().any())

#Drop the row of having less than three non-Null Values

print(df.dropna(thresh=3))

values={
    "A": 0,
    "B": 100,
    "C":200,
    "D":300
}

print(df.fillna(value= values))