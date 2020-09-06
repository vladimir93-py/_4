from itertools import count
for el in count(int(input('Введите начальное число'))):
    print(el, end='')
    quit = input()
    if quit == 'q':
        break