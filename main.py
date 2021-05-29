import pandas as pd
import matplotlib.pyplot as plt


# df_new = pd.read_csv('intermediate_res_2.csv',sep='|')
# df_new['name'] = df_new['name'].apply(lambda x: x.split(','))

df = pd.read_json('data/thailand_universities.json')
df = df[['name', 'state-province']]
y = df.groupby('state-province')['name'].apply( lambda x: ','.join(x.str.strip().replace(',',''))).reset_index()

df_grp = df.groupby(['state-province']).count().reset_index()
df_grp = df_grp.rename(columns={'name':'count'})
df_grp = df_grp.sort_values(by='count', ascending=False)
df_grp.to_csv('intermediate_res.csv',sep='|',index=False)
# fig = df_grp.plot.bar( x='state-province',y='name').get_figure()
# fig.savefig('test.jpg')
dff = pd.merge(df, df_grp, on='state-province').sort_values(by='count', ascending=False)
dff[['state-province','name','count']].to_csv('intermediate_res_1.csv',sep='|',index=False)

dff = pd.merge(y, df_grp, on='state-province').sort_values(by='count', ascending=False)
dff[['state-province','name','count']].to_csv('intermediate_res_2.csv',sep='|',index=False)

s = 2
