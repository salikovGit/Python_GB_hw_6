'''
6 - Сформировать список из N членов последовательности.
Для N = 5: 1, -3, 9, -27, 81 и т.д.
'''


def negafibonacci(n):
    return [(-3) ** i for i in range(n)]


print(negafibonacci(10))
