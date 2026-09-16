import numpy as np
import pandas as pd

data ={
    'City': ['London','New York','London','New York'],
    'Year':[2025,2025,2026,2026],
    'Sales' : [815,679,267,974]
}

df = pd.DataFrame(data)
pivot = df.pivot_table(values='Sales',index='City',columns='Year',aggfunc='sum')
print(pivot)