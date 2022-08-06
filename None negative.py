while True:
    try:
        num = int(input('Enter a negative integer: '))
        if num < 0:
            break
        else:
            print('Please input a negative integer.')
    except Value :
        print('Please input a negative integer.')

print('Output =', num)
