'''
1 - Определить, присутствует ли в заданном списке строк, некоторое число
'''


def is_here(strings_list, number):
    return number in [int(el) for el in strings_list if el.isdigit()]



print(is_here(['asd', 'dqwd', '5', '135', '', '12'], 12))
