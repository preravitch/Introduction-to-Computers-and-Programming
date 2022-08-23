x=input('Enter a comma-separated list: ').split(',')
list=[]
for i in x:
    for j in x:
        for k in x:
            m=[i,j,k]
            if j!= i and k!= i and k!= j:
                list.append(m)

for o in list:
    print(*o)