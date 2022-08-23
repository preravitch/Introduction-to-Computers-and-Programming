def func(x,y):
       
    if x > 15:
        a='x>15'
        z=y**2

    elif x<y:
        a='x<y'
        z=x**2-y**2
    elif y>10:
        a='y=10'
        z=x**2+y**2
    return a,z

x=int(input('Enter x: '))
y=int(input('Enter y: '))

b,d = func(x,y)

print(f'{b}:z={d}')