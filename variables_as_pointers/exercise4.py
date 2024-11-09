dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# Without running this code, what will it print? Why?

# it will print: [1, 42, 3]
# Line 7 is mutation: both variables point to the same objects.
# The list is shared
# So both are updated when key/value pair is mutated