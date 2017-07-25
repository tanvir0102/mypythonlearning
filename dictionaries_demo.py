#!/usr/bin/env python3

my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
print(my_dict['key1'])
my_dict = {'k1':123, 'k2':3.4, 'k3':'string'}
print(my_dict['k3'][::-1])

my_dict['k1'] = my_dict['k1'] - 120
print(my_dict['k1'])


my_dict['k1'] += 100
print(my_dict['k1'])

d = {}
d['animal'] = 'Dog'
d['answer'] = 42

print(d)
d = {'k1': {'nestkey': {'subnestkey': 'value'}}}
print(d['k1']['nestkey']['subnestkey'])

d['k1'] = 1
d['k2'] = 2
d['k3'] = 3

print(d.keys())
print(d.values())

print(d.items())
