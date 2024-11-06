# Which of the following values can't be used
# as a key in a dict object, and why?

'cat'                        # ok to use: immutable built-in
(3, 1, 4, 1, 5, 9, 2)        # ok to use: immutable
['a', 'b']                   # can't be used: mutable object
{'a': 1, 'b': 2}             # can't be used: mutable object  
range(5)                     # range is lazy sequence, can't be used # EDIT can be used, immutable.
{1, 4, 9, 16, 25}            # can't be used: mutable
3                            # ok: immutable.
0.0                          # ok: immutable
frozenset({1, 4, 9, 16, 25}) # ok: immutable