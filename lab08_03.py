def time(b):
    if b=='cake':
        print('The baking time of cake usually bake for 45 minutes')
    elif b=='cupcake':
        print('The baking time of cake usually bake for 45 minutes')
    elif b=='cookie':
        print('The baking time of cookie usually bake for 10 minutes')
    else:
        print("We don't know that recipe")
    return b
        

print('!!Welcome to Sweet Mania!!')
print('=======Let\'s Bake!=======')
print('==========================')

b=(input('What\'d we like to bake? (cake,cupcake,cookie) :'))
time(b)
