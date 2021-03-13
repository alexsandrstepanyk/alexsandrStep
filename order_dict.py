d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = {}
d2['a'] = 'B'
d2['b'] = 'A'
d2['c'] = 'C'

d3 = {}
d3['a'] = 'B'
d3['b'] = 'A'
d3['c'] = 'C'

d4 = {}
d4['a'] = 'B'
d4['b'] = 'A'
d4['c'] = 'C'
print(d1 == d2)
print(d1 == d3)
print(d2 == d4)

for k, v in d1.items():
    print(k, v)

from collections import OrderedDict
d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = OrderedDict()
d2['a'] = 'B'
d2['b'] = 'A'
d2['c'] = 'C'

d3 = OrderedDict()
d3['a'] = 'B'
d3['b'] = 'A'
d3['c'] = 'C'

d4 = OrderedDict()
d4['a'] = 'B'
d4['b'] = 'A'
d4['c'] = 'C'

print(d1 == d2)
print(d1 == d3)
print(d2 == d4)
print(d2 == d3)