import random

a = [False,True,True,None,True,None,None,False,False,None,True,False]
b = ["or","or","or","==","!=","==","and","==","!=","and","!=","and"]
c = [False,False,None,None,True,True,False,True,None,False,True,None]


for x in range(12):
    a1 = random.choice(a)
    b1 = random.choice(b)
    c1 = random.choice(c)
    if b1 == '!=':
        ans = bool(a1 != c1)
    elif b1 == '==':
        ans = bool(a1 == c1)
    elif b1 == 'or':
        ans = bool(a1 or c1)
    else:
        ans = bool(a1 and c1)
    print ('{} {} {}=>{}'.format(a1,b1,c1,ans))


# if b1 == '!=':
#     ans = a1 != c1
# elif b1 == '==':
#     ans = a1 = c1
# elif b1 == 'or':
#     ans = a1 or b1
# else:
#     ans = a1 and b1
# print(1 == 2)

# for x in range(10):
#     print((None and False), end='\n\n')
#     print(None)
#     a1 = random.choice(a)
#     b1 = random.choice(b)
#     c1 = random.choice(c)
#     s = '{} {} {}'.format(str(a1), b1, str(c1))
#     print(s)
#     ans = eval(s)
#     print(ans)
#     #print ('{} {} {}=>{}'.format(a1,b1,c1,ans))











# print('{}{}{}=>{}'.format(a,b,c,d))