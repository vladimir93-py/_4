from itertools import cycle
list = input('Введите список разделяя пробелом').split()
iter = cycle(list)
quit = None

while quit != 'q':
    print(next(iter), end='')
    quit = input()
