import pandas as pd
import numpy as np
import seaborn as sns


df = pd.read_json('data/statesDaily.json')
subset = df['state'].isin(['MA', 'WA', 'CA', 'NY'])
df = df[subset]
df = df.sort_values('date')

dateDict = {}
day = 1
for d in df['date']:
    if d not in dateDict:
        dateDict[d] = day
        day += 1

def dateConvert(date):
    return dateDict[date]

df['day'] = df['date'].apply(dateConvert)
df['logPositive'] = df['positive'].apply(np.log)

sns.lineplot('day', 'logPositive', data=df, hue='state')
sns.lineplot('day', 'positive', data=df, hue='state')
