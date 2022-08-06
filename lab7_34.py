def prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if (n%i) == 0:
                return False
        return True
n = int(input("Enter N: "))
for i in range (2,n+1):
    if prime(n):
        print(i)
