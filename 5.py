from functools import reduce

def list(el_1, el_2):
    return el_1 * el_2
my_list = [el for el in range(100, 1001, 100)]
print(f'Мой лист:\n{my_list}\nУмножение:\n{reduce(list, my_list)}')