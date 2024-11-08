# Write a find_integers function that returns a list
# of all the integers from my_tuple:

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

# def find_integers(iterable):
#     new_list = []
#     for member in iterable:
#         if type(member) is int:
#             new_list.append(member)
#     return new_list

def find_integers(iterable):
    return [ member
            for member in iterable
            if type(member) is int ]

integers = find_integers(my_tuple)
print(integers)


