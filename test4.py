# x = 1.12345

# print(f'{x:.2f}')


import sys


def start_function():
    a = input('What do you want to print? ')
    if a == 'RAINBOW':
        sys.stdout.write('\033[31mR\033[0m')
        sys.stdout.write('\033[32mA\033[0m')
        sys.stdout.write('\033[33mI\033[0m')
        sys.stdout.write('\033[34mN\033[0m')
        sys.stdout.write('\033[35mB\033[0m')
        sys.stdout.write('\033[31mO\033[0m')
        sys.stdout.write('\033[32mW\033[0m')

        print('\n')
    else:
        b = input('What color do you want? ')
        c = input('What kind of font/formatting do you want? ')
        d = input('What kind of background do you want? ')
        b = int(b)
        c = int(c)
        d = int(d)

        def white_colorful_text(a,b,c,d):
            print('\033[{1};{2};{3}m {0} \033[0m'.format(a,b,c,d))
        white_colorful_text(a,b,c,d)




start_function()

