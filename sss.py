xo = []
for i in range(9):
    v = input("Input: ")
    if v == 'x' or v == 'o':
        xo.append(v)
    else:
        print("Wrong Input")
        exit()

# print(xo)
index = 0
for row in range(3):
    print('-'*7)
    for col in range(3):
        print("|%s" % xo[index], end="")
        index += 1
    print("|")
print('-'*7)

######################################
import numpy as np
xo = np.array(xo)
xo = np.reshape(xo, (3, 3))
for row in range(3):
    print('-'*7)
    for col in range(3):
        print('|%s' % xo[row, col], end="")
    print("|")
print("-"*7)
