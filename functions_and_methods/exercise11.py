def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

# this would print:
# 42
# 3
# 2

# default parameter value for 2nd & 3rd (omitted) argument are used.
# Only the first argument is passed through to function.