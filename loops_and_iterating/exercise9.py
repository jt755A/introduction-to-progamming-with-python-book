# Write a function that computes and returns
# the factorial of a number by using a for or while loop.

# factorial works: n = index in range(index, 0, -1)
# or range(1, n + 1, 1)

# def factorial(n):
#     index = 1
#     workings = 1
#     while index <= n:
#         workings *= index
#         index += 1
#     return workings

# print(factorial(25))


def factorial(n):
    result = 1
    for number in range(1, n + 1):
        result *= number
    return result

print(factorial(7))