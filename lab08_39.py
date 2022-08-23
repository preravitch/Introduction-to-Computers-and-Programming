def gra(f1,f2,m):
    area=(6.672*(10**(-11))*f1*f2)/(m**2)
    return area
f1=int(input('Enter the weight of first object (kg.):'))
f2=int(input('Enter the weight of second object (kg.):'))
m=int(input('Enter distance between the objects (m.):'))

area = gra(f1,f2,m)

print(f'The gravity force between two objects is {area:.4f} newtons')