import math

x1 = "x\u2081"
x2 = "x\u2082"
# Welcome
print('Hi, Im a calculator for Pythagoras and Bashkara.')
print('This calculator was maded to simplificed the life of the studant')
print('Type only the numbers')
print('and this calculator was created by Gustavo Rocha Dück')

# Type of calculator
choise1 = str(input('Type p to Pythagoras and b to Bashkara: '))

# Calculator
if choise1 == 'p':
    choise01 = str(input('Type h to Hipotenusa to calculate the H and to the Cateto c: '))
    if choise01 == 'h':
        c1 = float(input('Type the Value of the first Cateto: '))
        c2 = float(input('Type the value of the second Cateto: '))
        cal1 = c1**2 + c2**2
        cal2 = math.sqrt(cal1)
        print(f'The value of the Hipotenuse is: {cal1}')
        print(f'The value of the Hipotenuse squered meters is: {cal2}')
        print('Thank for use this Calculator!!!')
        input('')
    elif choise01 == 'c':
        h1 = float(input('The Value of the Hipotenuse: '))
        c3 = float(input('The value of the Cateto:'))
        cal01 = h1**2 - c3**2
        cal02 = math.sqrt(cal01)
        print(f'The value of the Cateto is: {cal01}')
        print(f'THe volue of the Cateto squered meters is: {cal02}')
        print('Thank for use this Calculator!!!')
        input('')
    else:
        print('You type a Wrong key')
elif choise1 =='b':
    a = float(input('Type the value of A: '))
    b = float(input('Type the value of B: '))
    c = float(input('Type the value of C: '))
    #delta 
    delta01 = b**2 - 4 * a * c
    #bashkara
    b1 = (-b + math.sqrt(delta01)) / (2 * a)
    b2 = (-b - math.sqrt(delta01)) / (2 * a)
    print(f'The value of {x1} is: {b1}')
    print(f'The value of {x2} ​is: {b2}')
    print('Thank for use this Calculator!!!')
    input('')
else:
    print('You type a Wrong key')