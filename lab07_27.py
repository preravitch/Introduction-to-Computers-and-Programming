i = input("enter any number")
if i.isnumeric():
    i = float(i)
    if 0 <= i < 30:
        print("YOU FAILED THE COURSE")
    elif 30 <= i == 50:
        print("YOU PASSED THE COURSE")
    else:
        print("Invalid number")
        
