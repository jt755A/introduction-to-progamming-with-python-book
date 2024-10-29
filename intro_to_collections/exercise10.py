# Bob expects the following code to print the names in
# alphabetical order. Without running the code,
# can you say whether it will? Explain your answer.

names = { 'Chris', 'Clare', 'Karis', 'Karl',
          'Max', 'Nick', 'Victor' }
print(names)

# it is not guaranteed: sets are unordered collections.
# It's very unlikely to preserve the original order.
# The print order depends on internal python implementation,
# that may vary depending on version #.