
# # Data Analysis Examples
# ## 2012 Federal Election Commission Database

import pandas as pd

fec = pd.read_csv('datasets/fec/P00000001-ALL.csv', nrows=100)
fec.info()


#%%
#정당별 후보자별 기부금>0 인 관측치 counting
chunks = pd.read_csv('datasets/fec/P00000001-ALL.csv', chunksize=10000)
names = pd.Series([])
for i, c in enumerate(chunks):
    print(i)
    c = c[c['contb_receipt_amt']>0]
    names = names.add(c['cand_nm'].value_counts(), fill_value=0)
names.name = "Counts"
print(names)

#%%
parties = {'Bachmann, Michelle': 'Republican',
           'Cain, Herman': 'Republican',
           'Gingrich, Newt': 'Republican',
           'Huntsman, Jon': 'Republican',
           'Johnson, Gary Earl': 'Republican',
           'McCotter, Thaddeus G': 'Republican',
           'Obama, Barack': 'Democrat',
           'Paul, Ron': 'Republican',
           'Pawlenty, Timothy': 'Republican',
           'Perry, Rick': 'Republican',
           "Roemer, Charles E. 'Buddy' III": 'Republican',
           'Romney, Mitt': 'Republican',
           'Santorum, Rick': 'Republican'}

candinfo = pd.DataFrame(names)
candinfo.reset_index(inplace=True)

candinfo.rename(columns = {"index":"Candidate"}, inplace=True)
candinfo['party'] = candinfo["Candidate"].map(parties)

#%%
candinfo.groupby('party').sum()


#%%
# 직업/직장별 기부금 통계
fec.contbr_occupation.value_counts()[:10]
occ_mapping = {
   'INFORMATION REQUESTED PER BEST EFFORTS' : 'NOT PROVIDED',
   'INFORMATION REQUESTED' : 'NOT PROVIDED',
   'INFORMATION REQUESTED (BEST EFFORTS)' : 'NOT PROVIDED',
   'C.E.O.': 'CEO'
}

emp_mapping = {
   'INFORMATION REQUESTED PER BEST EFFORTS' : 'NOT PROVIDED',
   'INFORMATION REQUESTED' : 'NOT PROVIDED',
   'SELF' : 'SELF-EMPLOYED',
   'SELF EMPLOYED' : 'SELF-EMPLOYED',
}

# If no mapping provided, return x
f = lambda x: occ_mapping.get(x, x)
g = lambda x: emp_mapping.get(x, x)

chunks = pd.read_csv('datasets/fec/P00000001-ALL.csv', chunksize=10000)
data = pd.DataFrame()
for i, c in enumerate(chunks):
    print(i)
    c.contbr_occupation = c.contbr_occupation.map(f)
    c.contbr_employer = c.contbr_employer.map(g)
    c = c[['cand_nm','contb_receipt_amt','contbr_st','contb_receipt_dt','contbr_employer','contbr_occupation']]
    data = pd.concat([data, c])

print(data.shape)

#%%
data['party'] = data["cand_nm"].map(parties)
by_occupation = data.pivot_table('contb_receipt_amt',
                                index='contbr_occupation',
                                columns='party', aggfunc='sum')
over_2mm = by_occupation[by_occupation.sum(1) > 2000000]
print(over_2mm)
over_2mm.plot(kind='barh')


#%%
def get_top_amounts(group, key, n=5):
    totals = group.groupby(key)['contb_receipt_amt'].sum()
    return totals.nlargest(n)

grouped = data.groupby('cand_nm')
grouped.apply(get_top_amounts, 'contbr_occupation', n=7)
grouped.apply(get_top_amounts, 'contbr_employer', n=5)


#%%

import numpy as np
bins = np.array([0, 1, 10, 100, 1000, 10000,
                 100000, 1000000, 10000000])
labels = pd.cut(data.contb_receipt_amt, bins)
labels


grouped = data.groupby(['cand_nm', labels])
grouped.size().unstack(0)


# 주별 기부금 통계
#%%
grouped = data.groupby(['cand_nm', 'contbr_st'])
totals = grouped.contb_receipt_amt.sum().unstack(0).fillna(0)
totals = totals[totals.sum(1) > 100000]
totals[:10]

percent = totals.div(totals.sum(1), axis=0)
percent[:10]

#연도별 월별
data['date'] = pd.to_datetime(data.contb_receipt_dt)
