# age = int(input('How old are you? '))

# print(f'You are {age} years old.')
# print(f'In 10 years, you will be {age + 10} years old.')
# print(f'In 20 years, you will be {age + 20} years old.')
# print(f'In 30 years, you will be {age + 30} years old.')
# print(f'In 40 years, you will be {age + 40} years old.')

age = int(input('How old are you? '))

print(f'You are {age} years old.')

years = [10, 20, 30, 40]

for year in years:
    print(f'In {year} years, you will be {age + year} years old.')