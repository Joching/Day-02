import sys

arg = sys.argv
num = 0


for x in arg:
	print(f'argv of {num} is {x}')
	num = num + 1

arg.sort(key=len, reverse=True)

num = 0

for x in arg:
	print(x)