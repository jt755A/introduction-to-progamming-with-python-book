import copy

orig = [('a', 'b', 'c'), 5, 6]

dup = copy.deepcopy(orig)

print(id(orig[0]))
print(id(dup[0]))

print(orig[0] is dup[0])