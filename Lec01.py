
# ## Python Language Basics

# #### Indentation, not braces

# #### Variables and argument passing
#%%
a = [1, 2, 3]
b = a
a.append(4)
print(b)

#%%
def append_element(some_list, element):
    some_list.append(element)

data = [1, 2]
append_element(data, 3)
print(data)

# #### Dynamic references, strong types
#%%
a = 5
print(type(a))
a = 'foo'
print(type(a))

#%%
'5' + 5

#%%
a = 4.5
b = 2
# String formatting, to be visited later
print('a is {0}, b is {1}'.format(type(a), type(b)))
print(a / b)

#%%
a = 5
print(isinstance(a, int))

a = 5; b = 4.5
print(isinstance(a, float))
print(isinstance(b, (int, float)))


#%%
a = [1, 2, 3]
b = a
c = list(a)
print(a is b)
print(a is not c)
print(a == c)


#%%
a = None
print(a is None)


# #### Mutable and immutable objects
#%%
a_list = ['foo', 2, [4, 5]]
a_list[2] = (3, 4)
a_list

#%%
a_tuple = (3, 5, (4, 5))
a_tuple[1] = 'four'


# ### Scalar Types

# #### Numeric types
#%%
ival = 17239871
ival ** 6

fval = 7.243
fval2 = 6.78e-5


#%%
c = """
This is a longer string that
spans multiple lines
"""
c.count('\n')

#%%
a = 'this is a string'
a[10] = 'f'
b = a.replace('string', 'longer string')
b

#%%
a = 5.6
s = str(a)
print(s)

#%%
s = 'python'
print(list(s))
print(s[:3])

#%%
s = '12\\34'
print(s)

#%%
s = r'this\has\no\special\characters'
s

#%%
a = 'this is the first half '
b = 'and this is the second half'
a + b

#%%
template = '{0:.2f} {1:s} are worth US${2:d}'
template.format(4.5560, 'Argentine Pesos', 1)


# #### Bytes and Unicode
#%%
bytes_val = b'this is bytes'
bytes_val
decoded = bytes_val.decode('utf8')
decoded  # this is str (Unicode) now


# #### Booleans
#%%
s = '3.14159'
fval = float(s)
print(type(fval))
print(int(fval))
print(bool(fval))
print(bool(0))


# #### None
#%%
a = None
print(a is None)
b = 5
print(b is not None)
print(type(None))


# #### Dates and times
#%%
from datetime import datetime, date, time
dt = datetime(2011, 10, 29, 20, 30, 21)
dt.day
dt.minute

dt.date()
dt.time()

dt.strftime('%m/%d/%Y %H:%M')

datetime.strptime('20091031', '%Y%m%d')

dt.replace(minute=0, second=0)

dt2 = datetime(2011, 11, 15, 22, 30)
delta = dt2 - dt
delta
type(delta)

dt
dt + delta


# ### Control Flow
#%%
a = 5; b = 7
c = 8; d = 4
if a < b or c > d:
    print('Made it')

# #### for loops
sequence = [1, 2, None, 4, None, 5]
total = 0
for value in sequence:
    if value is None:
        continue
    total += value
print(total)

sequence = [1, 2, 0, 4, 6, 5, 2, 1]
total_until_5 = 0
for value in sequence:
    if value == 5:
        break
    total_until_5 += value
print(total_until_5)

#%%
for i in range(4):
    for j in range(4):
        if j > i:
            break
        print((i, j))


# #### while loops
x = 256
total = 0
while x > 0:
    if total > 500:
        break
    total += x
    x = x // 2
print(total)

# #### pass
if x < 0:
    print('negative!')
elif x == 0:
    # TODO: put something smart here
    pass
else:
    print('positive!')

# #### range
#%%
range(10)
print(list(range(10)))
print(list(range(0, 20, 2)))
print(list(range(5, 0, -1)))


seq = [1, 2, 3, 4]
for i in range(len(seq)):
    val = seq[i]
print(val)

sum = 0
for i in range(100000):
    # % is the modulo operator
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)


# #### Ternary expressions
#%%
x = 5
'Non-negative' if x >= 0 else 'Negative'

