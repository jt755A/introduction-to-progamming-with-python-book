# Write Python code to create a new tuple from
# (1, 2, 3, 4, 5). The new tuple should be in
# reverse order from the original. It should also exclude
# the first and last members of the original.
# The result should be the tuple (4, 3, 2).

my_tuple = (1, 2, 3, 4, 5)

# mytuple = list(mytuple) # converts to list.
# mytuple = mytuple[1:-1] # removes first and last object from list

# mytuple.reverse()       # reverses list: mutates collection
# mytuple = tuple(mytuple) # converts back into new tuple
# #print(mytuple)

result = my_tuple[-2:0:-1]
print(result)