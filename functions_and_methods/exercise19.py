def remainders_5(numbers):
    return [number % 5 for number in numbers]

#def divisible_5(numbers):
    if all(remainders_5(numbers)) != 0:
       return False
    else:
        return True

#def divisible_5(numbers):
    if any(remainders_5(numbers)) == 0:
        return True
    else:
        return False      

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

#numbers_test = [0] # Checking if 0 is divisible by 5 in test

#print(divisible_5(numbers_1))
#print(divisible_5(numbers_2))
#print(divisible_5(numbers_3))
#print(divisible_5(numbers_4))



print(all(remainders_5(numbers_1)))
print(all(remainders_5(numbers_2)))
print(all(remainders_5(numbers_3)))
print(all(remainders_5(numbers_4)))