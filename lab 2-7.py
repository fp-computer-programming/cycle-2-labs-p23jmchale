# Creator jmchale 9/22/2022

a = 5
b = 10
c = 0
d = -4

variables = [a,b,c,d]

for num in variables:
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')

    if num < -5:
        print(f'{num} is less than -5')
    elif num < 5:
        print(f'{num} is between -5 and 5')
    else:
        print(f'{num} is greater than 5')

    print('-----')