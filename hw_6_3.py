'''
3 - Найти расстояние между двумя точками пространства(числа вводятся через пробел)
'''


def distance():
    a = list(map(int, (input('Введите две координаты точки 1 через пробел\n').split(' '))))
    b = list(map(int, (input('Введите две координаты точки 2 через пробел\n').split(' '))))
    return ((b[0] - a[0])**2 + (b[1] - a[1])**2)**0.5


print(distance())