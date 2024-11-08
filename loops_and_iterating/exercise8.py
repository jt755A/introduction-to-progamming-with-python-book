# Write a comprehension that creates a dict object whose keys
# are strings and whose values are the length
# of the corresponding key. Only keys with odd lengths
# should be in the dict.
# Use the set given by my_set as the source of strings.

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',     # include
    'Cheddar',     # include
    'Cocoa',       # include
}

# for name in my_set:
#     print(f'{name} = {len(name)}')


odd_dict = { name: len(name)
            for name in my_set
            if len(name) % 2 == 1 }

print(odd_dict)