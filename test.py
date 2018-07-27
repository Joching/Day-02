a = 4+2j
print(type(a))

a = str(a)

print(type(a))
print(a)

print(a.replace('j','').replace('(','').replace(')','') + 'i')