x=str(input('Enter a string: '))
x= [i for i in x]
y=[]
print(x)
for a in x:
    if a.isupper():
        y.append(a.lower())
    elif a.islower():
        y.append(a.upper())
    else:
        y.append(a)
    
print('Reverse string ouput: ',*y,sep='')

        
      