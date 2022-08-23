print('======Car Slogan Program=====')
x=str(input('Enter Car Brand:'))
cars= x.split()
for i in (cars):
    if i == 'BMW'or i== 'bmw' :
     print('%s = Designed For Driving Pleasure'%i)
    elif i == 'Audi' or i == 'audi' :
        print('%s = Advancement Through Technology'%i)
    elif i == 'Lexus' or i == 'lexus' :
        print('%s = Pursuit of Perfection'%i)
    else :
        print('%s = Unknow Slogan'%i)