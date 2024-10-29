my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)
print(id(my_list), id(another_list))

print(my_list[3] is another_list[3])
# Given the above code, answer the following questions and explain your answers:

# 1. Are the lists assigned to my_list and another_list equal?
# Yes, because they lists are made up of identical members.

# 2. Are the lists assigned to my_list and another_list the same object?
# No, each list is a unique object: this can be verified with id()
# EDIT: List constructor creates new object

# 3. Are the nested lists at index 3 of my_list and another_list equal?
# Yes, because they are lists made up of identical elements.
# 4. Are the nested lists at index 3 of my_list and another_list the same object?
# Yes, list constructors make 'shallow copies': the individual elements are
# the same object ---> EDIT only a reference to the nested list gets copied.