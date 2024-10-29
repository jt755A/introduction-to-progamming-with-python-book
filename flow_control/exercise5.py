def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])        

# What does this code output, and why?

# Prints 'Empty' because [] is falsy. my_list looks for falsy in else block.
# if block looks for truthy: i.e. requires a non-empty, non-zero argument.
# EDIT: non-zero is fine. As long as list has element, it is falsy.
# Even if contains only falsy values.
