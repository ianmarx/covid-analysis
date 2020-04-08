import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_json('data/statesDaily.json')
df = df[df['state'] == 'MA']
df = df[df['positive'] >= 10]
df = df.sort_values('date')
df = df.reset_index()
df = df.rename(columns = {'index': 'oldIndex'})
df['day'] = df.index + 1

df['logPositive'] = df['positive'].apply(np.log)
df['logDeath'] = df['death'].apply(np.log)
df['posRate'] = df['positive'].pct_change()
df['deathRate'] = df['death'].pct_change()

sns.lineplot('day', 'logPositive', data=df)
sns.lineplot('day', 'posRate', data=df)
sns.lineplot('day', 'logDeath', data=df)
sns.lineplot('day', 'deathRate', data=df)
