import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta
from datetime import datetime

df = pd.read_csv(r'anime.csv')

def extract_ep(txt):
    check = False
    data = ""

    for i in txt:
        if i == ')':
            break
        if i == '(':
            check = True
            continue
        if check:
            data += i

    return data

def extraction_time(txt):
    data = ""

    for i in range(len(txt)):
        if txt[i] == ')':
            for j in range(i+1, i + 20):
                data += txt[j]

            return data

def calculate_total_months(period):
    try:
        start_str, end_str = period.split(' - ')
        
        start_date = datetime.strptime(start_str, '%b %Y')
        end_date = datetime.strptime(end_str, '%b %Y')
        
        r = relativedelta(end_date, start_date)
        
        return r.years * 12 + r.months + 1

    except:
        return None

df["Episodes"]= df['Title'].apply(extract_ep)
df['Episodes'] = df['Episodes'].str.replace("eps","")
df['Episodes'] = df['Episodes'].astype(int)
df["Timeframe"]= df['Title'].apply(extraction_time)
df['Total Months'] = df['Timeframe'].apply(calculate_total_months)
print(df)
print("\nSeries with Highest Score: ")
print(df[df['Score'] == df['Score'].max()]['Title'])
print("\nSeries with most Episodes: ")
print(df[df['Episodes'] == df['Episodes'].max()]['Title'])