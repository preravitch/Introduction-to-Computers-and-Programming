l=['Apple','Banana','Orange','Grape','Mango','Kiwi']

for a in l:
    x=len(a)
    if x >=6:
        print(f'{a} is 6 characters or more!')
    else:
        print(f'{a} is only {x} long!')