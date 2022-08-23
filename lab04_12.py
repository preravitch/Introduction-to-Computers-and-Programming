d=int(input('Please enter the distance:'))
m=str(input('By taxi or motorbike:'))
if m=="taxi":
    if d<=20 and d>0:
        p=100
    elif d>=21:
        p=500
    else:
        print('Error')
    
elif m=="motorbike":
    if d<=20 and d>0:
        p=150
    elif d>=21:
        
        p=600
    else:
        print('Error')

else:
    print('Error')

print(f'The delivery charge is {p}baht')