import numpy as np
import math as m

p1 = input('Input coordinate of P1: ').split()
p2 = input('Input coordinate of P2: ').split()
p3 = input('Input coordinate of P3: ').split()
p1 = [int(x) for x in p1]
p2 = [int(x) for x in p2]
p3 = [int(x) for x in p3]
p1 = np.array(p1)
p2 = np.array(p2)
p3 = np.array(p3)
d1 = m.sqrt(np.sum((p1-p2)**2))
d2 = m.sqrt(np.sum((p2-p3)**2))
d3 = m.sqrt(np.sum((p3-p1)**2))

list_d=[]
list_d.append(d1)
list_d.append(d2)
list_d.append(d3)
print(f'Output :\n The longest distance ={max(list_d):.2f}')