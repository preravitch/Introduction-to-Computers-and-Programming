

def check(n):
    ans=0
    if n%2==0:
        ans='even'
    elif n%2!=0:
        ans='odd'
    return ans
        
try:
    
    x=int(input('Enter an interger number: '))
    ans=check(x)
    print(f'{x} is an {ans} number.')
        
except:
    print('Invalid input')
