#%%
import pandas as pd

#%%
d = pd.read_csv('./data/1583129.csv')

#%%
d = d[d.DATE.str.contains('-12-24')]

#%%
def is_snow(v):
    if v >= 1:
        return 1
    else:
        return 0
#%%
d['snih'] = d.SNWD.apply(lambda x: is_snow(x))

#%%
d.groupby('NAME').snih.value_counts(normalize=True).to_excel('na-blate-NOAA.xlsx')