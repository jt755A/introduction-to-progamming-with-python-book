# Print all of the even numbers in the following list
# of nested lists. This time, don't use any for loops.

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

# print(len(my_list)) # 3

# outer_index = 0
# while outer_index < len(my_list):
    
#     inner_index = 0
#     while inner_index < len(my_list[outer_index]):
#         if my_list[outer_index][inner_index] % 2 == 0:
#             print(my_list[outer_index][inner_index])
#         inner_index += 1

#     outer_index += 1


outer_index = 0
while outer_index < len(my_list):
    inner_index = 0
    while inner_index < len(my_list[outer_index]):
        number = my_list[outer_index][inner_index]
        if number % 2 == 0:
            print(number)
        inner_index += 1

    outer_index += 1