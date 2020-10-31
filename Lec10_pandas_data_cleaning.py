# # Data Cleaning and Preparation
import numpy as np
import pandas as pd
PREVIOUS_MAX_ROWS = pd.options.display.max_rows
pd.options.display.max_rows = 20
np.random.seed(12345)
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(10, 6))
np.set_printoptions(precision=4, suppress=True)


# ## Handling Missing Data
string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
string_data
string_data.isnull()

string_data[0] = None
string_data.isnull()


# ### Filtering Out Missing Data
from numpy import nan as NA
data = pd.Series([1, NA, 3.5, NA, 7])
data.dropna()
data[data.notnull()]

data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],
                     [NA, NA, NA], [NA, 6.5, 3.]])

data.dropna()
data.dropna(how='all')

data[4] = NA
data
data.dropna(axis=1, how='all')


# ### Filling In Missing Data
df = data
df.fillna(0)
df.fillna({1: 0.5, 2: 0})
df.fillna(0, inplace=True)
df

#%%
df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = NA
df.iloc[4:, 2] = NA
df
df.fillna(method='ffill')
df.fillna(method='ffill', limit=2)

#%%
data = pd.Series([1., NA, 3.5, NA, 7])
data.fillna(data.mean())


# ## Data Transformation
# ### Removing Duplicates

#%%
data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                     'k2': [1, 1, 2, 3, 3, 4, 4]})
data
data.duplicated()
data.drop_duplicates()


# ### Transforming Data Using a Function or Mapping
#%%
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                              'Pastrami', 'corned beef', 'Bacon',
                              'pastrami', 'honey ham', 'nova lox'],
                     'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
data

meat_to_animal = {
  'bacon': 'pig',
  'pulled pork': 'pig',
  'pastrami': 'cow',
  'corned beef': 'cow',
  'honey ham': 'pig',
  'nova lox': 'salmon'
}

lowercased = data['food'].str.lower()
lowercased
data['animal'] = lowercased.map(meat_to_animal)
data

#Or
data['food'].map(lambda x: meat_to_animal[x.lower()])



# ### Renaming Axis Indexes
#%%
data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                    index=['Ohio', 'Colorado', 'New York'],
                    columns=['one', 'two', 'three', 'four'])

transform = lambda x: x[:4].upper()
data.index = data.index.map(transform)
data


#%%
data.rename(index={'OHIO': 'INDIANA'},
            columns={'three': 'peekaboo'})

data.rename(index={'OHIO': 'INDIANA'}, inplace=True)
data


# ### Discretization and Binning
#%%
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
cats

cats.codes
cats.categories
pd.value_counts(cats)

#%%
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
pd.cut(ages, bins, labels=group_names)


# ### Permutation and Random Sampling

df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
df.sample(n=3)

#%%
choices = pd.Series([5, 7, -1, 6, 4])
draws = choices.sample(n=10, replace=True)
draws





#%%
#Movies Dataset
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('datasets/movielens/movies.dat', sep='::',
                       header=None, names=mnames)
movies[:10]


all_genres = []
for x in movies.genres:
    all_genres.extend(x.split('|'))
genres = pd.unique(all_genres)
genres

zero_matrix = np.zeros((len(movies), len(genres)))
dummies = pd.DataFrame(zero_matrix, columns=genres)

for i, gen in enumerate(movies.genres):
    indices = dummies.columns.get_indexer(gen.split('|'))
    dummies.iloc[i, indices] = 1

movies_windic = movies.join(dummies.add_prefix('Genre_'))
movies_windic.iloc[0]





