import pandas as pd

df = pd.read_csv('dk_cities_fixed.csv')
df = df.set_index('City')
df = df.drop('No.', axis=1)

# IN PANDAS CONDITIONAL SLICING USE THE FOLLOWING:
# and ->  &
# or  ->  |
small = df.loc[df['2017'] < 10000]
medium = df.loc[(df['2017'] > 10000) & (df['2017'] < 50000)]
large = df.loc[(df['2017'] > 50000)]

dp_small = (small['2017'] - small['2006']).mean()
dp_medium = (medium['2017'] - medium['2006']).mean()
dp_large = (large['2017'] - large['2006']).mean()

df_dp = pd.DataFrame(data=[dp_small, dp_medium, dp_large],
                     columns=['Pop.inc./dec.'],
                     index=['<10000', '10000-50000', '>50000'])

print(df_dp)
