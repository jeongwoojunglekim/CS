# # Built-in Data Structures, Functions, 
# ## Data Structures and Sequences
# ### Tuple

#%%
tup = 4, 5, 6
print(tup)

nested_tup = (4, 5, 6), (7, 8)
print(nested_tup)

tuple([4, 0, 2])  #list를 tuple로 전환
tup = tuple('string')
print(tup)
print(tup[0])

#mutable vs. immutable
#%%
tup = tuple(['foo', [1, 2], True])
tup[2] = False    #error: tuple은 값을 변경할 수 없음
tup[1].append(3)  #가능: tup[1]이 가리키는 것은 [1,2] 의 주소값임. 주소값을 변경하는 것은 아니기 때문에 가능.
tup


tup = (4, None, 'foo') + (6, 0) + ('bar',)
print(tup)
print(('foo', 'bar') * 4)


# #### Unpacking tuples
#%%
tup = (4, 5, 6)
a, b, c = tup
print(b)

tup = 4, 5, (6, 7)
a, b, (c, d) = tup
print(d)

a, b = 1, 2
print(a,b)
b, a = a, b
print(a,b)

seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print('a={0}, b={1}, c={2}'.format(a, b, c))


# ### List
#%%
a_list = [2, 3, 7, None]

tup = ('foo', 'bar', 'baz')
b_list = list(tup)
print(b_list)

b_list[1] = 'peekaboo'
print(b_list)

gen = range(10)
print(list(gen))


# #### Adding and removing elements
#%%
b_list.append('dwarf')
print(b_list)

b_list.insert(1, 'red')
print(b_list)

b_list.pop(2)
print(b_list)

b_list.append('foo')
print(b_list)
b_list.remove('foo')
print(b_list)


#%%
print('dwarf' in b_list)
print('dwarf' not in b_list)


# #### Concatenating and combining lists
#%%
[4, None, 'foo'] + [7, 8, (2, 3)]
x = [4, None, 'foo']
x.extend([7, 8, (2, 3)]) #append와 다름
print(x)


# #### Sorting
#%%
a = [7, 2, 5, 1, 3]
a.sort()
print(a)

b = ['saw', 'small', 'He', 'foxes', 'six']
b.sort(key=len)
print(b)



# #### Slicing
#%%
seq = [7, 2, 3, 7, 5, 6, 0, 1]
seq[1:5]
seq[3:4] = [6, 3]
print(seq)
print(seq[:5])
print(seq[3:])
print(seq[-4:])
print(seq[-6:-2])
print(seq[::2])
print(seq[::-1])


# ### Built-in Sequence Functions
#%%
some_list = ['foo', 'bar', 'baz']
mapping = {}
for i, v in enumerate(some_list):
    mapping[v] = i
print(mapping)

# #### zip
#%%
seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
zipped = zip(seq1, seq2)
print(list(zipped))

seq3 = [False, True]
list(zip(seq1, seq2, seq3))

for i, (a, b) in enumerate(zip(seq1, seq2)):
    print('{0}: {1}, {2}'.format(i, a, b))



# ### dict
#%%
empty_dict = {}
d1 = {'a' : 'some value', 'b' : [1, 2, 3, 4]}
d1[7] = 'an integer'
print(d1)
print(d1['b'])
print('b' in d1)

d1[5] = 'some value'
d1['dummy'] = 'another value'
print(d1)

#%%
keys = list(d1.keys())
values = list(d1.values())
print(keys, values)

#%%
del d1[5]
print(d1)
ret = d1.pop('dummy')
print(ret, d1)

#%%
d1.update({'b' : 'foo', 'c' : 12})
print(d1)

#%%
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)
by_letter

#%%
d = {}
d[tuple([1, 2, 3])] = 5
print(d)


# ### set
#%%
s1 = set([2, 2, 2, 1, 3, 3])
s2 = {2, 2, 2, 1, 3, 3}
print(s1, s2)

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}

a.union(b)
a | b

a.intersection(b)
a & b


# ### List, Set, and Dict Comprehensions
#%%
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
upper = [x.upper() for x in strings if len(x) > 2]
print(upper)

unique_lengths = {len(x) for x in strings}
print(unique_lengths)

loc_mapping = {val : index for index, val in enumerate(strings)}
print(loc_mapping)


# #### Nested list comprehensions
#%%
all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],
            ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
result = [name for names in all_data for name in names
          if name.count('e') >= 2]
print(result)

#%%
some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [x for tup in some_tuples for x in tup]
print(flattened)

print([[x for x in tup] for tup in some_tuples])


# ## Functions
#%%
def my_function(x, y, z=1.5):
    if z > 1:
        return z * (x + y)
    else:
        return z / (x + y)

my_function(5, 6, z=0.7)
my_function(3.14, 7, 3.5)
my_function(10, 20)

# ### Namespaces, Scope, and Local Functions
#%%
def func():
    a = []
    for i in range(5):
        a.append(i)

a = []
def func():
    for i in range(5):
        a.append(i)

a = None
def bind_a_variable():
    global a
    a = []
bind_a_variable()
print(a)


#%%
#error
a = 10
def f():
    print(a)
    a = 20
    print(a)

f()


# ### Returning Multiple Values
#%%
def f():
    a = 5
    b = 6
    c = 7
    return a, b, c

a, b, c = f()
return_value = f()

def f():
    a = 5
    b = 6
    c = 7
    return {'a' : a, 'b' : b, 'c' : c}


# ### Anonymous (Lambda) Functions
#%%
def short_function(x):
    return x * 2

equiv_anon = lambda x: x * 2

def apply_to_list(some_list, f):
    return [f(x) for x in some_list]

ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2)



# ### Errors and Exception Handling
#%%
float('1.2345')
float('something')

def attempt_float(x):
    try:
        return float(x)
    except:
        return x

attempt_float('1.2345')
attempt_float('something')

#%%
float((1, 2))

def attempt_float(x):
    try:
        return float(x)
    except ValueError:
        return x

attempt_float((1, 2))


def attempt_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return x


# ## Files and the Operating System
#%%

path = 'examples/segismundo.txt'
f = open(path)
lines = [x.rstrip() for x in f]
print(lines)
f.close()


#%%
with open(path) as f:
    lines = [x.rstrip() for x in f]


#%%
with open('tmp.txt', 'w') as handle:
    handle.writelines(x for x in open(path) if len(x) > 1)
with open('tmp.txt') as f:
    lines = f.readlines()
print(lines)


# ### Bytes and Unicode with Files
#%%
with open(path) as f:
    chars = f.read(10)
print(chars)

with open(path, 'rb') as f:
    data = f.read(10)
print(data)

print(data.decode('utf8'))
print(data[:4].decode('utf8'))

