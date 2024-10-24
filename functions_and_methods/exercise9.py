def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

# should print:
# 42
# 3.141592
# 2.718
# the default parameter values were overwritten by explicit arguments