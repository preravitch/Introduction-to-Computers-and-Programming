import math
a=int(input('Enter degrees of angle: '))
b=math.radians(a)
sin=math.sin(b)
cos=math.cos(b)
tan=math.tan(b)
print(f'Value of sin({a}) is %.2f'%sin)
print(f'Value of cos({a}) is %.2f'%cos)
print(f'Value of tan({a}) is %.2f'%tan)