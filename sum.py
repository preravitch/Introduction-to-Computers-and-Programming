num=[]
while True:
    try:
        n=input('Enter a positive num (DONE=exit): ')
        if n== 'DONE':
            break
        n=int(n)
        if n>0:
            num.append(n)
    except:
        print('Invalid input')
print(f'Input list =',num)
print('Sum = ',sum(num))

            
            
