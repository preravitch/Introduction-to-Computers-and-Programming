def shape(n):
    if n=='c':
        r=float(input('Enter the radius of circle:'))
        area=m.pi*(r**2)
        
        print(f'The area of this circle is {area:.2f}')
    elif n=='t':
        b=float(input('Enter the base of triangle:'))
        h=float(input('Enter the height of triangle:'))
        area=1/2*b*h
        print(f'The area of this triangle is {area}')
    elif n=='r':
        b=float(input('Enter the width of rectangle:'))
        h=float(input('Enter the length of rectangle:'))
        area=b*h
        print(f'The area of this rectangle is {area}')
    return 


import math as m

what=input('Enter the shape c or t or r:')

shape(what)
