# Write a function that takes a single integer argument
# and prints a message that describes whether:

# the value is between 0 and 50 (inclusive)
# the value is between 51 and 100 (inclusive)
# the value is greater than 100
# the value is less than 0

# def number_range(int):
#     if int < 0:
#         print(f'{int} is less than 0')
#     elif 0 <= int <= 50:
#         print(f'{int} is between 0 and 50')
#     elif 51 <= int <= 100:
#         print(f'{int} is between 51 and 100')
#     else:
#         print(f'{int} is greater than 100')

# solution above is redundant: by ordering the if and elif
# statements, you can above the multiple <= number <= x

def number_range(number):
    if number < 0:
        print(f'{number} is less than 0')
    elif number <= 50:
        print(f'{number} is between 0 and 50')
    elif number <= 100:
        print(f'{number} is between 51 and 100')
    else:
        print(f'{number} is greater than 100')

number_range(0)
number_range(25)
number_range(50)
number_range(75)
number_range(100)
number_range(101)
number_range(-1)


# def number_range(number):
#     match number:
#         case < 0:
#             print(f'{number} is less than 0')
#         case >= 0 | <= 50:
#             print(f'{number} is between 0 and 50')
#         case >= 51 | <= 100:
#             print(f'{number} is between 51 and 100')
#         case > 100:
#             print(f'{number} is greater than 100')


# number_range(-1)