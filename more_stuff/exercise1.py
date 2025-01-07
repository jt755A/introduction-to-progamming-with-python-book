def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))

# What does the following function do?
# Be sure to identify the output value.

# 1. Takes a dictionary that is passed to function
# 2. Sorts it by key
# 3. Takes the 2nd value/index
# 4. passes this to a .upper method
# 5. This value is returned
# 6. (Value above is printed)

# Answer: 'CHRIS'