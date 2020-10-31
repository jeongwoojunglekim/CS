# # Computation on NumPy Arrays: Universal Functions
#%%
import numpy as np
np.random.seed(0)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output
        
values = np.random.randint(1, 10, size=5)
print(compute_reciprocals(values))
print(1.0 / values)

#%%
big_array = np.random.randint(1, 100, size=1000000)
#timeit

#%%
# n/(n+1)
np.arange(5) / np.arange(1, 6)


#%%
x = np.arange(9).reshape((3, 3))
2 ** x


#%%
x = np.arange(4)
print("x     =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2)  # floor division
print("-x     = ", -x)
print("x ** 2 = ", x ** 2)
print("x % 2  = ", x % 2)

-(0.5*x + 1) ** 2

#%%
# ### Absolute value
x = np.array([-2, -1, 0, 1, 2])
np.abs(x)


# ### Trigonometric functions
theta = np.linspace(0, np.pi, 3)
print("theta      = ", theta)
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))


x = [-1, 0, 1]
print("x         = ", x)
print("arcsin(x) = ", np.arcsin(x))
print("arccos(x) = ", np.arccos(x))
print("arctan(x) = ", np.arctan(x))


# ### Exponents and logarithms
x = [1, 2, 3]
print("x     =", x)
print("e^x   =", np.exp(x))
print("2^x   =", np.exp2(x))
print("3^x   =", np.power(3, x))


# The inverse of the exponentials, the logarithms, are also available.
x = [1, 2, 4, 10]
print("x        =", x)
print("ln(x)    =", np.log(x))
print("log2(x)  =", np.log2(x))
print("log10(x) =", np.log10(x))


#%%
# sum
L = np.random.random(100)
sum(L)
np.sum(L)

#%%
big_array = np.random.rand(1000000)
#timeit

# ## Minimum and Maximum
min(big_array), max(big_array)
np.min(big_array), np.max(big_array)


#%%
# ### Multi dimensional aggregates
# 
# One common type of aggregation operation is an aggregate along a row or column.
# Say you have some data stored in a two-dimensional array:

M = np.random.random((3, 4))
print(M)
M.sum()
M.min(axis=0)
M.max(axis=1)

# ### Other aggregation functions
# 
# |Function Name      |   NaN-safe Version  | Description                                   |
# |-------------------|---------------------|-----------------------------------------------|
# | ``np.sum``        | ``np.nansum``       | Compute sum of elements                       |
# | ``np.prod``       | ``np.nanprod``      | Compute product of elements                   |
# | ``np.mean``       | ``np.nanmean``      | Compute mean of elements                      |
# | ``np.std``        | ``np.nanstd``       | Compute standard deviation                    |
# | ``np.var``        | ``np.nanvar``       | Compute variance                              |
# | ``np.min``        | ``np.nanmin``       | Find minimum value                            |
# | ``np.max``        | ``np.nanmax``       | Find maximum value                            |
# | ``np.argmin``     | ``np.nanargmin``    | Find index of minimum value                   |
# | ``np.argmax``     | ``np.nanargmax``    | Find index of maximum value                   |
# | ``np.median``     | ``np.nanmedian``    | Compute median of elements                    |
# | ``np.percentile`` | ``np.nanpercentile``| Compute rank-based statistics of elements     |
# | ``np.any``        | N/A                 | Evaluate whether any elements are true        |
# | ``np.all``        | N/A                 | Evaluate whether all elements are true        |




# ## Example: What is the Average Height of US Presidents?
#%%
import pandas as pd
data = pd.read_csv('data/president_heights.csv')
heights = np.array(data['height(cm)'])
print(heights)

print("Mean height:       ", heights.mean())
print("Standard deviation:", heights.std())
print("Minimum height:    ", heights.min())
print("Maximum height:    ", heights.max())
print("25th percentile:   ", np.percentile(heights, 25))
print("Median:            ", np.median(heights))
print("75th percentile:   ", np.percentile(heights, 75))

#%%
import matplotlib.pyplot as plt
import seaborn; seaborn.set()  # set plot style
plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number')


#%%
a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
a + b
a + 5

M = np.ones((3, 3))
M
M + a

a = np.arange(3)
b = np.arange(3)[:, np.newaxis]

print(a)
print(b)
a + b




M = np.ones((2, 3))
a = np.arange(3)
M + a

a = np.arange(3).reshape((3, 1))
b = np.arange(3)
a + b

M = np.ones((3, 2))
a = np.arange(3)
M + a

a[:, np.newaxis].shape
M + a[:, np.newaxis]

#%%
X = np.random.random((10, 3))
Xmean = X.mean(0)
X_centered = X - Xmean
X_centered.mean(0)

#%%
# x and y have 50 steps from 0 to 5
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]
z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

import matplotlib.pyplot as plt
plt.imshow(z, origin='lower', extent=[0, 5, 0, 5], cmap='viridis')
plt.colorbar();









