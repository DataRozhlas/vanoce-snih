#%%
import pandas as pd
import os

#%%
out = {}
for f in os.listdir('data'):
    if f.endswith('.xls'):
        tmp = pd.read_excel('data/' + f, skiprows=3, sheetname='celková výška sněhu')
        tmp = tmp[tmp['měsíc'] == 12]
        for rok in tmp.iterrows():
            r = rok[1]['rok']
            s = rok[1]['24.']
            if f not in out:
                out[f] = {}
            out[f][r] = s

#%%
blato = {}
for s in out:
    blato[s] = {'snih': 0, 'blato': 0}
    for rok in out[s].values():
        if rok > 0:
            blato[s]['snih'] += 1
        else:
            blato[s]['blato'] += 1

#%%
o = pd.DataFrame.from_dict(blato, orient='index')

#%%
o['snih_pct'] = o.apply(lambda row: (row['snih'] / (row['snih'] + row['blato'])) * 100 , axis=1)

#%%
o.to_excel('na-blate.xlsx')

#%%
pd.DataFrame.from_dict(out, orient='index').to_excel('na-blate-roky.xlsx')
