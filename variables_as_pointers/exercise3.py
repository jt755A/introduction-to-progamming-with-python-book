dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

# Without running this code, what will it print? Why?

# it will print 'The Life of Brian'.
# dict2 is created using a dict constructor on dict1.
# This means that a new dict object will be created
# in the heap, that has the same value as dict1, but
# is a distinct object, at a distinct address.
#( dict1 and dict2 will contain different pointers in their
# own stack address.)

# Therefore, a change made to dict2 will not be reflected
# in dict.

print(id(dict1["Monty Python"]), id(dict2["Monty Python"]))