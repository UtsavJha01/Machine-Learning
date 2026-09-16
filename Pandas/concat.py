import numpy as np
import pandas as pd

df1 = pd.DataFrame({
    'Utsav':["Virat",29]
})
df2 = pd.DataFrame({
    'Utsav':["Minakshi",43]
})

print(pd.concat([df1,df2]))
print(pd.concat([df1,df2],axis=1))