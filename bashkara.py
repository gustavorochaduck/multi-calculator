import math

a = float(input('Value of A: '))
b = float(input('Value of B: '))
c = float(input('Value of C: '))

delta = b**2 - 4*a*c

if delta < 0:
    print('The equation does not have real roots.')
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f'The value of x1: {x1}')
    print(f'The value of x2: {x2}')