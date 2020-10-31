
import numpy as np
import pandas as pd

# use pandas to extract rainfall inches as a NumPy array
rainfall = pd.read_csv('data/Seattle2014.csv')['PRCP'].values
inches = rainfall / 254.0  # 1/10mm -> inches
inches.shape

import matplotlib.pyplot as plt
import seaborn; seaborn.set()  # set plot styles
plt.hist(inches, 40)

# ### Digging into the data
x = np.array([1, 2, 3, 4, 5])
x < 3  # less than
x > 3  # greater than
x <= 3  # less than or equal
x >= 3  # greater than or equal
x != 3  # not equal
x == 3  # equal


# It is also possible to do an element-wise comparison of two arrays, and to include compound expressions:
(2 * x) == (x ** 2)
# 
# | Operator	    | Equivalent ufunc    || Operator	   | Equivalent ufunc    |
# |---------------|---------------------||---------------|---------------------|
# |``==``         |``np.equal``         ||``!=``         |``np.not_equal``     |
# |``<``          |``np.less``          ||``<=``         |``np.less_equal``    |
# |``>``          |``np.greater``       ||``>=``         |``np.greater_equal`` |



# ### Counting entries
np.sum(x < 6)
np.sum(x < 6, axis=1)
np.any(x > 8)
np.any(x < 0)
np.all(x < 10)
np.all(x == 6)

np.all(x < 8, axis=1)
np.sum((inches > 0.5) & (inches < 1))
np.sum(~( (inches <= 0.5) | (inches >= 1) ))

print("Number days without rain:      ", np.sum(inches == 0))
print("Number days with rain:         ", np.sum(inches != 0))
print("Days with more than 0.5 inches:", np.sum(inches > 0.5))
print("Rainy days with < 0.2 inches  :", np.sum((inches > 0) &
                                                (inches < 0.2)))


# ## Boolean Arrays as Masks
x[x < 5]
rainy = (inches > 0)
days = np.arange(365)
summer = (days > 172) & (days < 262)

print("Median precip on rainy days in 2014 (inches):   ",
      np.median(inches[rainy]))
print("Median precip on summer days in 2014 (inches):  ",
      np.median(inches[summer]))
print("Maximum precip on summer days in 2014 (inches): ",
      np.max(inches[summer]))
print("Median precip on non-summer rainy days (inches):",
      np.median(inches[rainy & ~summer]))


# ## Aside: Using the Keywords and/or Versus the Operators &/|
A = np.array([1, 0, 1, 0, 1, 0], dtype=bool)
B = np.array([1, 1, 1, 0, 1, 1], dtype=bool)
A | B
A or B

x = np.arange(10)
(x > 4) & (x < 8)
(x > 4) and (x < 8)


#%%

# # Fancy Indexing

import numpy as np
rand = np.random.RandomState(42)

x = rand.randint(100, size=10)
print(x)

[x[3], x[7], x[2]]

ind = [3, 7, 4]
x[ind]

ind = np.array([[3, 7],
                [4, 5]])
x[ind]


X = np.arange(12).reshape((3, 4))
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
X[row, col]


X[row[:, np.newaxis], col]

row[:, np.newaxis] * col

print(X)


X[2, [2, 0, 1]]

X[1:, [2, 0, 1]]


# And we can combine fancy indexing with masking:

mask = np.array([1, 0, 1, 0], dtype=bool)
X[row[:, np.newaxis], mask]


mean = [0, 0]
cov = [[1, 2],
       [2, 5]]
X = rand.multivariate_normal(mean, cov, 100)
X.shape

import matplotlib.pyplot as plt
import seaborn; seaborn.set()  # for plot styling
plt.scatter(X[:, 0], X[:, 1])

#%%
indices = np.random.choice(X.shape[0], 20, replace=False)
indices

selection = X[indices]  # fancy indexing here
selection.shape

plt.scatter(X[:, 0], X[:, 1], alpha=0.3)
plt.scatter(selection[:, 0], selection[:, 1],
            facecolor='none', s=200)


            
# ## Modifying Values with Fancy Indexing

x = np.arange(10)
i = np.array([2, 1, 8, 4])
x[i] = 99
print(x)

x[i] -= 10
print(x)

x = np.zeros(10)
x[[0, 0]] = [4, 6]
print(x)


i = [2, 3, 3, 4, 4, 4]
x[i] += 1
x


x = np.zeros(10)
np.add.at(x, i, 1)
print(x)

np.random.seed(42)
x = np.random.randn(100)

# compute a histogram by hand
bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)

# find the appropriate bin for each x
i = np.searchsorted(bins, x)

# add 1 to each of these bins
np.add.at(counts, i, 1)

plt.plot(bins, counts, linestyle='steps')

#%%

x = np.array([2, 1, 4, 3, 5])
np.sort(x)
x.sort()
print(x)

x = np.array([2, 1, 4, 3, 5])
i = np.argsort(x)
print(i)
x[i]


# ### Sorting along rows or columns
rand = np.random.RandomState(42)
X = rand.randint(0, 10, (4, 6))
print(X)
np.sort(X, axis=0)
np.sort(X, axis=1)

X = rand.rand(10, 2)

import matplotlib.pyplot as plt
import seaborn; seaborn.set() # Plot styling
plt.scatter(X[:, 0], X[:, 1], s=100)

dist_sq = np.sum((X[:, np.newaxis, :] - X[np.newaxis, :, :]) ** 2, axis=-1)

# for each pair of points, compute differences in their coordinates
differences = X[:, np.newaxis, :] - X[np.newaxis, :, :]
differences.shape


sq_differences = differences ** 2
sq_differences.shape

dist_sq = sq_differences.sum(-1)
dist_sq.shape

dist_sq.diagonal()


nearest = np.argsort(dist_sq, axis=1)
print(nearest)


K = 2
nearest_partition = np.argpartition(dist_sq, K + 1, axis=1)


plt.scatter(X[:, 0], X[:, 1], s=100)

K = 2

for i in range(X.shape[0]):
    for j in nearest_partition[i, :K+1]:
        # plot a line from X[i] to X[j]
        # use some zip magic to make it happen:
        plt.plot(*zip(X[j], X[i]), color='black')