m=int(input('Enter a sale amount> '))
if m>=0 and m<=5000:
    d=5
elif m>=5001 and m<=30000:
    d=10
else:
    d=15
print('')
dis=m*(d)/100
print(f'Discount= {dis:.2f}')
pay=m-dis
print(f'You pay only {pay:.2f}')
