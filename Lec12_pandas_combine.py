
import numpy as np
import pandas as pd

# ## Hierarchical Indexing
data = pd.Series(np.random.randn(9),
                 index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                        [1, 2, 3, 1, 3, 1, 2, 2, 3]])

data.index
data['b']
data['b':'c']
data.loc[['b', 'd']]
data.loc[:, 2]

data.unstack()
data.unstack().stack()


#%%
frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'],
                              ['Green', 'Red', 'Green']])
frame

frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
frame

# ### Reordering and Sorting Levels
frame.swaplevel('key1', 'key2')
frame.sort_index(level=1)
frame.swaplevel(0, 1).sort_index(level=0)


#%%
# ## Combining and Merging Datasets


# ### Concatenating Along an Axis
arr = np.arange(12).reshape((3, 4))
arr
np.concatenate([arr, arr], axis=1)


#%%


s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])

pd.concat([s1, s2, s3])
pd.concat([s1, s2, s3], axis=1)

s4 = pd.concat([s1, s3])
s4
pd.concat([s1, s4], axis=1)
pd.concat([s1, s4], axis=1, join='inner')

pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']])
result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
result
result.unstack()

pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three'])


#%%

df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],
                   columns=['one', 'two'])
df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],
                   columns=['three', 'four'])
df1
df2
pd.concat([df1, df2], axis=1, keys=['level1', 'level2'])



# ### Pivoting “Long” to “Wide” Format

#%%

data = pd.read_csv('examples/macrodata.csv')
data.head()
periods = pd.PeriodIndex(year=data.year, quarter=data.quarter,
                         name='date')
columns = pd.Index(['realgdp', 'infl', 'unemp'], name='item')
data = data.reindex(columns=columns)
data.index = periods.to_timestamp('D', 'end')
ldata = data.stack().reset_index().rename(columns={0: 'value'})


ldata[:10]

pivoted = ldata.pivot('date', 'item', 'value')
pivoted

ldata['value2'] = np.random.randn(len(ldata))
ldata[:10]

pivoted = ldata.pivot('date', 'item')
pivoted[:5]
pivoted['value'][:5]


unstacked = ldata.set_index(['date', 'item']).unstack('item')
unstacked[:7]


# ### Pivoting “Wide” to “Long” Format

# In[ ]:


df = pd.DataFrame({'key': ['foo', 'bar', 'baz'],
                   'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})
df
melted = pd.melt(df, ['key'])
melted

reshaped = melted.pivot('key', 'variable', 'value')
reshaped

