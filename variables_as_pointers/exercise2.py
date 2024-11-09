# Without running this code, what will it print? Why?

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

# it will print: {42, 'Monty Python', ('a', 'b', 'c'),
#                 range(5, 10)}
# order may be different.

# set2 contains same pointers as set1. So when set1
# is mutated, set2 reflects the changes made to set1.

# Ie. set1 and set2 are aliases for the same object