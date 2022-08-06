a,b=0,1
print(a)
print(b)
while b<= 100:
    t=b
    b=a+b
    a=t
    if b<= 100:
        print(b,end=' ')
print()

fib=[0,1]
while fib[-1]<=100:
    n=fib[-1] + fib[-2]
    if n<= 100:
        fib.append(n)
    else:
        break
print(' '.join([str(x) for x in fib]))
