# In your own words, explain the difference between these two expressions.

my_object1 == my_object2
my_object1 is my_object2

# first line means that both expressions have the same value/evaluate
# to the same value

# second line means both expressions reference/point to the same object.
# i.e. they share the same object. 
# The pointer in stack address (that both expressions themselves point to)
# points to the exact same address in the heap.


# EDIT: 1st line compares the 2 to see if equal. Considered equal when
# they have the same value/state. Compares value equality.
# If two objects REPRESENT the same VALUE.
# For collections, they are the same
# when they have the same elements.

# EDIT: 2nd line: checks two variables to see if they reference the same
# object.
# If so, my_object1 and my_object2 are ALIASES for the same object