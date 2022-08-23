x=str(input('Enter string1: '))
y=str(input('Enter string1: '))
z=str(input('Enter string1: '))

b=[x,y,z]
b.sort(key=len)

long=b[-1]
short=b[0]

print(f'The longest string is {long}')
print(f'The shortest string is {short}')