def DuoChars(ch1,ch2,n):
    for i in range(n):
        print(ch1,end="")
        print(ch2,end='')

x=input('Enter the first character (ch1): ')
y=input('Enter the second character (ch2): ')
z=int(input('Enter the number (n): '))
z=z/2
z=int(z)
print()
DuoChars(x,y,z)
