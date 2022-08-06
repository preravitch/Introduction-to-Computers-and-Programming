nums=[]
odd=[]
even=[]

while True:
    try:

        n=int(input('Enter an interger (-999 to end): '))

        if n==-999:
            break

        nums.append(n)

    except ValueError:
        print('Error: this is not an interger')

for i in nums:
    if i%2==0:
        even.append(i)

    elif i%2!=0:
        odd.append(i)

print('The number of odd numbers = ', len(odd))
print('The number of even numbers = ', len(even))
        

    

    
