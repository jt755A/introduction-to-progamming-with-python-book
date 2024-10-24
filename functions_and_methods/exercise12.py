def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# this would throw an error: expects an argument
# for parameter 1 (no default parameter)