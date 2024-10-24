def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')

# This will return an exception/error: it expects 2 "positional" arguments
# (because there are 2 parameters in the definition), there is 
# only 1.
# foo() missing 1 required positional argument: 'qux'

# Pass parameters to a call to print twice.