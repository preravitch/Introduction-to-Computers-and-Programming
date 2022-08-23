e=False
l=[]
c=[]
k=[]
while e==False:
    x=str(input('enter name: '))
    
    if x=='done':
        e=True
        break
        
    l.append(x)

for i in l:
    if l.count(i) >1:
        c.append(i)
for a in c:
    if not a in k:
        k.append(a)


print('name list is ',l)
print('duplicated name list is ',k)
