import math
x1,y1,z1 =input('Enter the first point: ').split()
x2,y2,z2 =input('Enter the second point: ').split()
x1,y1,z1,x2,y2,z2 =int(x1),int(y1),int(z1),int(x2),int(y2),int(z2)
a=((x1-x2)**2)+((y1-y2)**2)+((z1-z2)**2)
d=math.sqrt(a)
print(f'The distance between ({x1}, {y1}, {z1}) and ({x2}, {y2}, {z2}) is {d:.2f}')