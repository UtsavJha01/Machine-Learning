import numpy as np
import pandas as pd

print("Using Dictionary: ")
data={
    "name":["Utsav", "Tony","Peter","Virat"],
    "age" :[21,19,24,38],
    "city":["Motihari", "Bhagalpur","Queens","London"],
}

df = pd.DataFrame(data)
print(df)

print("Using Data List: ")

data_list=[
    ['Utsav',21,'Motihari'],
    ['Tony',19,'Bhagalpur'],
    ['Peter',24,'Queens'],
    ['Virat',38,'London']
]
df2=pd.DataFrame(data_list)
print(df2)

print("Using Costomized Column: ")
columns = ["Name","Age","City"]
df2=pd.DataFrame(data_list,columns= columns)
print(df2)

print(df.loc[0])
print(df.loc[[0,1]])

df2["Profession"] =['Student','Student','Actor','Cricketer']
print(df2)

print(df2.drop('Profession',axis=1,inplace=True))
