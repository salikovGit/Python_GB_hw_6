'''
5 - Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
'''


def pair_multiply(numbers_list):
    return [numbers_list[i] * numbers_list[-1 - i] for i in range(len(numbers_list) // 2 + len(numbers_list) % 2)]


print(pair_multiply([1, 2, 3, 4, 5]))
