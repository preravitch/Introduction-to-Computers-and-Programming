def area(x):
    a=(0.433)*(x**2)*6
    return a

try:
    r=int(input('Enter side(s):'))
    a = area(r)
    print(f'The area of the regular hexagon is {a:.2f}')

except:
    print('Invalid input')
