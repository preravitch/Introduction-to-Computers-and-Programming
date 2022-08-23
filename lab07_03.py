list1=[]
count=0
while True:
    x=float(input('Enter score: '))
    list1.append(x)
    count+=1
    y=str(input('Do you want to enter another score? y/n: '))

    if y=='n':
        break
    elif y!='y':
        print('Invalid input')
        break
print()
print('The average score is ',(sum(list1))/count)
