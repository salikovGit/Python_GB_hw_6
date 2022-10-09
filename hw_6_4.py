'''
4 - Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
Примеры
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1
'''


def second_entry(strings_list, element):
    try:
        position = len(strings_list[:strings_list.index(element)]) + 1 + strings_list[strings_list.index(element) + 1::].index(element)
        return position
    except ValueError:
        return -1


print(second_entry(["qwe", "asd", "zxc", "qwe", "ertqwe"], "qwe"))
print(second_entry(["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], "йцу"))
print(second_entry(["йцу", "фыв", "ячс", "цук", "йцукен"], "йцу"))
print(second_entry([], "qwe"))
