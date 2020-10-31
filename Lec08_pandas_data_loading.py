
# # Data Loading, Storage, 
import numpy as np
import pandas as pd
np.random.seed(12345)
import matplotlib.pyplot as plt

# ## Reading and Writing Data in Text Format
df = pd.read_csv('examples/ex1.csv')
print(df)

df2 = pd.read_csv('examples/ex2.csv', header=None)
df3 = pd.read_csv('examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])

names = ['a', 'b', 'c', 'd', 'message']
df4 = pd.read_csv('examples/ex2.csv', names=names, index_col='message')


#%%
parsed = pd.read_csv('examples/csv_mindex.csv',
                     index_col=['key1', 'key2'])
print(parsed)

#%%
result = pd.read_table('examples/ex3.txt', sep='\s+')
result


#%%
ex4 = pd.read_csv('examples/ex4.csv', skiprows=[0, 2, 3])


#%%

# ### Reading Text Files in Pieces
result = pd.read_csv('examples/ex6.csv')
pd.read_csv('examples/ex6.csv', nrows=5)


chunker = pd.read_csv('examples/ex6.csv', chunksize=1000)

tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)

tot = tot.sort_values(ascending=False)
tot[:10]


#%%
# ### Writing Data to Text Format
dates = pd.date_range('1/1/2000', periods=7)
ts = pd.Series(np.arange(7), index=dates)
ts.to_csv('tseries.csv')

#%%
# ### JSON Data
obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
              {"name": "Katie", "age": 38,
               "pets": ["Sixes", "Stache", "Cisco"]}]
}
"""

import json
result = json.loads(obj)
result

asjson = json.dumps(result)

siblings = pd.DataFrame(result['siblings'], columns=['name', 'age'])
siblings


#%%
data = pd.read_json('examples/example.json')
data

print(data.to_json())
print(data.to_json(orient='records'))


# ### XML and HTML: Web Scraping
tables = pd.read_html('examples/fdic_failed_bank_list.html')
len(tables)
failures = tables[0]
failures.head()

close_timestamps = pd.to_datetime(failures['Closing Date'])
close_timestamps.dt.year.value_counts()

#%%
from lxml import objectify

path = 'datasets/mta_perf/Performance_MNR.xml'
parsed = objectify.parse(open(path))
root = parsed.getroot()

data = []

skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ',
               'DESIRED_CHANGE', 'DECIMAL_PLACES']

for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag] = child.pyval
    data.append(el_data)

perf = pd.DataFrame(data)
perf.head()


#%%


from io import StringIO
tag = '<a href="http://www.google.com">Google</a>'
root = objectify.parse(StringIO(tag)).getroot()
root.get('href')
root.text


# ## Binary Data Formats

#%%
frame = pd.read_csv('examples/ex1.csv')
frame.to_pickle('examples/frame_pickle')
pd.read_pickle('examples/frame_pickle')



# ### Reading Microsoft Excel Files
#%%

xlsx = pd.ExcelFile('examples/ex1.xlsx')
pd.read_excel(xlsx, 'Sheet1')

frame = pd.read_excel('examples/ex1.xlsx', 'Sheet1')
frame


#%%
writer = pd.ExcelWriter('examples/ex2.xlsx')
frame.to_excel(writer, 'Sheet1')
writer.save()

frame.to_excel('examples/ex2.xlsx')


# ## Interacting with Web APIs
#%%
import requests
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
resp

data = resp.json()
data[0]['title']

issues = pd.DataFrame(data, columns=['number', 'title',
                                     'labels', 'state'])
issues

