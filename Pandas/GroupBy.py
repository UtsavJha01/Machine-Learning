import numpy as np
import pandas as pd

df = pd.DataFrame({
    'City':['Paris','Paris','London','London'],
    'sales':[200,250,300,400]
})
print(df.groupby('City')['sales'].sum())


#Aggregation

print(df['sales'].mean())