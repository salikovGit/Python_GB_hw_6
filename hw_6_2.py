'''
2 - Найти сумму чисел списка стоящих на нечетной позиции
'''



def odd_sum(numbers_list):
    return sum([number for number in numbers_list[::2]])


print(odd_sum([1, 2, 3, 4, 5, 6, 7]))
