def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)

# This will return an exception/error: it expects 2 arguments
# (because there are 2 parameters in the definition) there are
# 3 arguments provided. ("3 arguments passed to function")
# Also, different data types: arguments in line 5 are int/float types,
# placeholders are str types.