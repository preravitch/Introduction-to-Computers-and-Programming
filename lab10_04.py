import numpy as np 

D = np.loadtxt("sales.tsv", delimiter='\t', dtype=int)
sales = D[:, 1:]
branch = D[:,0]
sum_per_branch = np.sum(sales, axis=1)  
sort=np.argsort(sum_per_branch)
print('Branch Products')
for i in range(1,np.shape(D)[0]+1):
    print(f'{branch[sort[-i]]}    {sum_per_branch[sort[-i]]}')


