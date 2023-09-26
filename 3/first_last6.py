# Задание №2
# Разработайте тесты для метода firstLast6, где на вход подается массив чисел, а метод
# возвращает true, если первое или последнее число в массиве равно 6, иначе false.

START = 0
END = -1


def first_last6(num_list: list) -> bool:
    assert type(num_list) == list, 'необходимо ввести массив целых чисел'
    return num_list[START] == 6 or num_list[END] == 6


if __name__ == '__main__':
    list_1 = [1, 2, 3, 4]
    list_2 = [6, 9, 5]
    list_3 = [5, 4, 6]
    print(first_last6(list_3))
    