def multiply(left, right): # 
    return left * right # 

def get_num(prompt): #
    return float(input(prompt)) # 

first_number = get_num('Enter the first number: ') # 
second_number = get_num('Enter the second number: ') #
product = multiply(first_number, second_number) # 
print(f'{first_number} * {second_number} = {product}') # 

# function names
# multiply: defined in 1, invoked in 9
# product = 9, 10
# EDITED: float built-in function used on line 5
# EDITED: input built-in function used on line 5

# parameter names
# left, right: defined on 1, used on 2
# prompt: defined in 4, used in 5



# Variables
# first_number = 7, 9, 10
# second_number = 8, 9, 10
# get_num: defined in 4, used on 7, 8