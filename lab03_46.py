import math

d = int(input('Please input demand: '))
k = int(input('Please input ordering cost: '))
h = float(input('Please input holding cost: '))
print('The optimal quantity is ', math.ceil(math.sqrt(2*d*k/h)))