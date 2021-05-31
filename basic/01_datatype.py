# *********************************
# ============Data Type============

'''
Python has 5 standard types.
    scalar
        ML
            Numbers: int(16 bits), float(32 bits), complex
        NL
            String: str( = [' ', ' ', ' ',...]): It has a list of characters structure,
                                                 thus, it is either scalar or vector.
    vector
        sequential
            list, tuple     : var., const.
        hash
            dictionary, set : var., const.
'''
lst = ['abc', 786, 2.24, 'john', 78.2]
tiny_lst = [123, 'john']
# List
lst.append('100')
print(lst)
lst += tiny_lst
for i, j in enumerate(lst):
    if j == 786:
        del lst[i]
print(lst)

# Tuple
tup = ('abc', 786, 2.23, 'john', 70.2)
tiny_tup = (123, 'john')
tup += '100',
print(tup)
tup = tup + tiny_tup
for i, j in enumerate(tup):
    if j == 786:
        tup = tup[:i] + tup[i + 1:]

# Dictionary
dt = {'abc': 786, 'john': 70.2}
tiny_dt = {'홍': '30세'}
dt['tom'] = '100'
print(dt)
for k, v in tiny_dt.items():
    dt[k] = v
del dt['abc']

# Set
st = {'a', 'b', 'c'}
tiny_st = {'e'}
st.add('d')
print(st)
st.update(tiny_st)
st.remove('c')
