""" An OrderedDict is a dict that remembers the order that keys were first inserted. If a new entry overwrites an existing entry,
the original insertion position is left unchanged. Deleting an entry and reinserting it will move it to the end."""

import collections

print ('Ordered dictionary:')
d1 = collections.OrderedDict()
d1['b'] = 'B'
d1['a'] = 'A'
d1['d'] = 'D'
d1['e'] = 'E'
d1['c'] = 'C'
for k, v in d1.items():
    print (k, v)

print ('\nOrderedDict:')
d2= collections.OrderedDict()
d2['a'] = 'A'
d2['b'] = 'B'
d2['c'] = 'C'
d2['d'] = 'D'
d2['e'] = 'E'

for k, v in d2.items():
    print(k, v)

#equality : it will check the order of insertion also while comparing

print(d1==d2)