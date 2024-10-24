foo = 'bar'

def set_foo():
    foo = 'qux'
    #print(id(foo))

set_foo()
print(foo)  
#print(id(foo))   #should print 'bar' which is local to function
# Foo variable on line 4 shadows shadows foo variable on line 1. 'qux' is local scope only.