def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# this would throw an error: expects an argument
# for parameter #3 (no default parameter)
# EDIT all subsequent lines must have default values
# This is a SyntaxError: doesn't even invoke the function