# In this problem, you should write code that creates a new list
# with one element for each number in my_list.
#  If the original number is an even, then the corresponding
#  element in the new list should contain the string 'even';
#  otherwise, the element should contain 'odd'.

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

# new_list = []

# for member in my_list:
#     if member % 2 == 0:
#         new_list.append('even')
#     else:
#         new_list.append('odd')



# print(new_list)

def even_or_odd(number):
    return 'even' if number % 2 == 0 else 'odd'
result = [ even_or_odd(number)
          for number in my_list ]
print(result)