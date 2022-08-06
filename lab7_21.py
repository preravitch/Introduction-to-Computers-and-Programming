while True :
    n = input('Enter an integer number: ')
    if n.isdigit():
        n=int(n)
        for i in range(n):
            for o in range(n):
                if (i+o)%2 != 0 :
                    print("x", end=" ")
                else :
                    print("o", end=" ")
            print()
        print()
    elif n == "x":
        break
    else :
        print ()
        
    
