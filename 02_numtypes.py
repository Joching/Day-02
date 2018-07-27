import sys


nume = sys.argv[1]
den = sys.argv[2]

nume = int(nume)
den = int(den)


print (f'{nume}/{den}')





ans = nume//den
rem = nume%den

print(ans)


print(f'{nume} divided by {den} equals {ans} with a remainder of {rem}')

#---------------------------

a = 42
b = 42-2j
c = 4+2j
d = 4.2
var = 0

varlist = ['a','b','c','d']
intvarlist = [a,b,c,d]


typelist = [type(a),type(b),type(c),type(d)]


for types in typelist:
	if types == int:
		print(f'Variable {varlist[var]} conatins: {intvarlist[var]} which is of type: Interger')
	elif types == float:
		print(f'Variable {varlist[var]} conatins: {intvarlist[var]} which is of type: Float')
	elif types == complex:
		intvarlist[var] = str(intvarlist[var])
		intvarlist[var] = intvarlist[var].replace('j','i').replace('(','').replace(')','') 
		print(f'Variable {varlist[var]} conatins: {intvarlist[var]} which is of type: Complex')
	var = var + 1












# print(f'Variable a contains: {a} which is of type: {type(a)}')
# print(f'Variable a contains: {b} which is of type: {type(b)}')
# print(f'Variable a contains: {c} which is of type: {type(c)}')
# print(f'Variable a contains: {d} which is of type: {type(d)}')

# atype = type(a)
# bbtype = type(b)
# ctype = type(c)
# dtype = type(d)


# 	if types == int:
# 		print('interger')
# 	elif types == float:
# 		print('float')




# numlist = ['a','b','c','d']


