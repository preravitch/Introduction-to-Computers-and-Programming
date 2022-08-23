while True:
    x=int(input('Select polygon shape to be calculated...'))
    if x==1:
        b=int(input('Input b = '))
        h=int(input('Input h = '))
        print('Area of triangle is ',0.5*b*h)
    elif x==2:
        w=int(input('Input w = '))
        h=int(input('Input h = '))
        print('Area of rectangle is ',w*h)
    elif x==3:
        a=int(input('Input a = '))
        b=int(input('Input b = '))
        h=int(input('Input h = '))
        print('Area of trapezoid is ',0.5*(a+b)*h)
    elif x==4:
        a=int(input('Input a = '))
        b=int(input('Input b = '))
        print('Area of ellipse is ',3.14*a*b)
    elif x==-9:
        break
