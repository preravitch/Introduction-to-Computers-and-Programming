# Accept initial balance
while True:
    try:
        b = int(input("Enter the initial balance: "))
        break
    except:
        print("Invalid input")
# Repeatedly accept transaction type and amount
while True:
    try:
        x, y = input("Transaction type and amount (\"done 0\" to exit): ").split()
        y = int(y)
        if y < 0:
            print("Invalid transaction!")
            continue
        if x.lower() == 'd':
            b += y
            print("> Deposit = %d THB, current balance = %d THB." % (y, b))
        elif x.lower() == 'w':
            if b >= y:
                b -= y
                print("> Withdrawal = %d THB, current balance = %d THB." % (y, b))
            else:
                print("Invalid transaction!")
        elif x.lower() == 'done':
            print("> Current balance = %d THB." % b)
            break
        else:
            print("Invalid transaction!")
    except:
        print("Invalid transaction!")
