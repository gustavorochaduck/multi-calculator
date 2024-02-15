import math

a = float(input('Value of A: '))
b = float(input('Value of B: '))
c = float(input('Value of C: '))

delta = b**2 - 4*a*c

if b <= 0:
    cal1 = (b + math.sqrt(delta)) / (2*a)
    cal2 = (b - math.sqrt(delta)) / (2*a)
    print(f'The value of x1: {cal1}')
    print(f'The value of x2: {cal2}')
    input('')
else:
    cal01 = (-b + math.sqrt(delta)) / (2*a)
    cal02 = (-b - math.sqrt(delta)) / (2*a)
    print(f'The value of x1: {cal01}')
    print(f'The value of x2: {cal02}')
    input('')
