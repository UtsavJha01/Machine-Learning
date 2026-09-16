import numpy as np
import pandas as pd

df1 = pd.DataFrame({
    'Name' : ['Utsav','Tony','Peter']
})

df2 = pd.DataFrame({
    'Reg' : [22,29,43]
})

print(df1)
print(df2)

print(df1.join(df2))
