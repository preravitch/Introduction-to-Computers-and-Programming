def point(a,b,c,d):
    ans=(((a-b)**2)+((c-d)**2))**0.5
    print(f'Distance between ({a},{c}) and ({b},{d}) = {ans:.2f}')

    return ans

a=int(input('Enter x of point 1: '))
c=int(input('Enter y of point 1: '))
b=int(input('Enter x of point 2: '))

d=int(input('Enter y of point 2: '))

point(a,b,c,d)


    