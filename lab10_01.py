import numpy as np
lists=[]
s=int(input('Input size of matrix: '))

for i in range(1,s+1):
    for c in range(1,s+1):
        x=int(input(f'Input the element at row {i} column {c}: '))
        lists.append(x)

new=np.reshape(lists,(s,s))

print('Matrix =')
print(new)

print('Determination =', np.linalg.det(new))

if np.linalg.det(new) != 0:
    C = np.linalg.inv(new)
    print('Inverse matrix =')
    print(C)
else:
    print('It is not invertible')
    