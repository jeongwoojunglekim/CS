{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 \
import numpy as np\
\
\
# ## Creating Arrays from Python Lists\
np.array([1, 4, 2, 5, 3])\
np.array([3.14, 4, 2, 3])\
np.array([1, 2, 3, 4], dtype='float32')\
np.array([range(i, i + 3) for i in [2, 4, 6]])\
np.zeros(10, dtype=int)\
np.ones((3, 5), dtype=float)\
np.full((3, 5), 3.14)\
\
np.arange(0, 20, 2)\
np.linspace(0, 1, 5)\
\
#random\
np.random.random((3, 3))\
np.random.normal(0, 1, (3, 3))\
np.random.randint(0, 10, (3, 3))\
\
# Create a 3x3 identity matrix\
np.eye(3)\
\
# Create an uninitialized array of three integers\
# The values will be whatever happens to already exist at that memory location\
np.empty(3)\
\
\
# ## NumPy Standard Data Types\
\
# np.zeros(10, dtype=np.int16)\
# ```\
\
# | Data type	    | Description |\
# |---------------|-------------|\
# | ``bool_``     | Boolean (True or False) stored as a byte |\
# | ``int_``      | Default integer type (same as C ``long``; normally either ``int64`` or ``int32``)| \
# | ``intc``      | Identical to C ``int`` (normally ``int32`` or ``int64``)| \
# | ``intp``      | Integer used for indexing (same as C ``ssize_t``; normally either ``int32`` or ``int64``)| \
# | ``int8``      | Byte (-128 to 127)| \
# | ``int16``     | Integer (-32768 to 32767)|\
# | ``int32``     | Integer (-2147483648 to 2147483647)|\
# | ``int64``     | Integer (-9223372036854775808 to 9223372036854775807)| \
# | ``uint8``     | Unsigned integer (0 to 255)| \
# | ``uint16``    | Unsigned integer (0 to 65535)| \
# | ``uint32``    | Unsigned integer (0 to 4294967295)| \
# | ``uint64``    | Unsigned integer (0 to 18446744073709551615)| \
# | ``float_``    | Shorthand for ``float64``.| \
# | ``float16``   | Half precision float: sign bit, 5 bits exponent, 10 bits mantissa| \
# | ``float32``   | Single precision float: sign bit, 8 bits exponent, 23 bits mantissa| \
# | ``float64``   | Double precision float: sign bit, 11 bits exponent, 52 bits mantissa| \
# | ``complex_``  | Shorthand for ``complex128``.| \
# | ``complex64`` | Complex number, represented by two 32-bit floats| \
# | ``complex128``| Complex number, represented by two 64-bit floats| \
\
\
\
#%%\
np.random.seed(0)  # seed for reproducibility\
\
x1 = np.random.randint(10, size=6)  # One-dimensional array\
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array\
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array\
\
\
# Each array has attributes ``ndim`` (the number of dimensions), ``shape`` (the size of each dimension), and ``size`` (the total size of the array):\
print("x3 ndim: ", x3.ndim)\
print("x3 shape:", x3.shape)\
print("x3 size: ", x3.size)\
print("dtype:", x3.dtype)\
\
# ## Array Indexing: Accessing Single Elements\
x1[0]\
x1[4]\
x1[-1]\
x1[-2]\
x2[0, 0]\
x2[2, 0]\
x2[2, -1]\
\
x2[0, 0] = 12\
print(x2)\
\
x1[0] = 3.14159  # this will be truncated!\
print(x1)\
\
#%%\
# ## Array Slicing: Accessing Subarrays\
x = np.arange(10)\
print(x)\
\
x[:5]  # first five elements\
x[5:]  # elements after index 5\
x[4:7]  # middle sub-array\
x[::2]  # every other element\
x[1::2]  # every other element, starting at index 1\
x[::-1]  # all elements, reversed\
x[5::-2]  # reversed every other from index 5\
\
\
# ### Multi-dimensional subarrays\
x2[:2, :3]  # two rows, three columns\
x2[:3, ::2]  # all rows, every other column\
x2[::-1, ::-1]\
\
\
# #### Accessing array rows and columns\
print(x2[:, 0])  # first column of x2\
print(x2[0, :])  # first row of x2\
print(x2[0])  # equivalent to x2[0, :]\
\
\
# ### Subarrays as no-copy views\
print(x2)\
x2_sub = x2[:2, :2]\
print(x2_sub)\
\
x2_sub[0, 0] = 99\
print(x2_sub)\
print(x2)\
\
#%%\
# ### Creating copies of arrays\
\
x2_sub_copy = x2[:2, :2].copy()\
print(x2_sub_copy)\
x2_sub_copy[0, 0] = 42\
print(x2_sub_copy)\
print(x2)\
\
#%%\
# ## Reshaping of Arrays\
grid = np.arange(1, 10).reshape((3, 3))\
print(grid)\
\
x = np.array([1, 2, 3])\
x.reshape((1, 3))\
\
x[np.newaxis, :]\
x.reshape((3, 1))\
x[:, np.newaxis]\
\
#%%\
# ## Array Concatenation and Splitting\
\
x = np.array([1, 2, 3])\
y = np.array([3, 2, 1])\
np.concatenate([x, y])\
\
\
# You can also concatenate more than two arrays at once:\
z = [99, 99, 99]\
print(np.concatenate([x, y, z]))\
\
\
\
grid = np.array([[1, 2, 3],\
                 [4, 5, 6]])\
np.concatenate([grid, grid])\
np.concatenate([grid, grid], axis=1)\
\
#%%\
# For working with arrays of mixed dimensions, it can be clearer to use the ``np.vstack`` (vertical stack) and ``np.hstack`` (horizontal stack) functions:\
\
x = np.array([1, 2, 3])\
grid = np.array([[9, 8, 7],\
                 [6, 5, 4]])\
np.vstack([x, grid])\
\
y = np.array([[99],\
              [99]])\
np.hstack([grid, y])\
\
\
}