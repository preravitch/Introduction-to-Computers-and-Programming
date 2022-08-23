import math
a=int(input('Enter the first number  :'))
b=int(input('Ebter the secound number:'))
c=((math.pow(a+b,2))-math.pow(a,3))/math.sqrt(math.fabs(a+b))
print(f'The result is:{c:.2f}')