x=str(input('Enter dd/mm/yyyy: '))
if len(x)==8:
    d=x[0:2]
    m=x[2:4]
    y=x[4:8]
    s=m
    s,y=int(s),int(y)
    if s>12:
        print('Error! There\'re 12 months')
    else:
        print(f'Date = {d}')
        print(f'Month = {m}')
        y-=543
        print(f'Year = {y}')

else :
    print('Please enter 8 digits!!')