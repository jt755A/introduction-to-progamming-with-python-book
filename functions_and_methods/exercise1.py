def set_foo():
    foo = 'bar'

set_foo()
print(foo) #will throw error: NameError: name 'foo' is not defined. foo is only defined locally, not globally.