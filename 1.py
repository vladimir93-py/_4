#print('Расчет заработной платы')
#a = int(input('Введите количество отработанных часов за месяц'))
#k = int(input('Введите ставку в час'))
#i = int(input('Введите фиксированную премиальную часть'))
#print(f'Ваша заработная плата состовляет: {(a * k) + i}')

from sys import argv
def salary():
    try:
        time, stavka, premia = map(float, argv[1:])
        print(f"Salary - {time * stavka + premia}")
    except ValueError:
        print("Enter all 3 numbers. Not string or empty characters")

salary()


