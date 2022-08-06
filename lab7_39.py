a=0
b=0
l=[]
while True:
    x=input('Add name: ')

    if x=='x':
        break

    l.append(x)

for i in l:
    b+=len(i)

    if len(i)>a:
        a=len(i)
        long=i
print()
print('List of name(s): ',l)
print(f'The length of 5 names is {b} characters')
print(f'The longest name is {long} with length of {a} characters.')
        


    
