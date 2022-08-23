import math as m
while True :
    x= int(input("Enter a number (n) :"))
    if x >= 0:
        ans = m.factorial(x)
        print(f'{x}! is {ans}')
        print()
    elif x == -1:
        print('Bye!!')
        break
        
    
    
    
