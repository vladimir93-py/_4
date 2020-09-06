def fact(el):
    f_el = 1
    if el == 0:
        yield f'{el}! = 1'
    for i in range(1, el + 1):
        f_el *= i
        yield f'{i}! = {f_el}'

for gen in fact(int(input('Факториал: '))):
    print(gen)