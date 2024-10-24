def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# this would print:
# 42
# 3.141592
# 2

# default parameter value for 3rd (omitted) argument is used.