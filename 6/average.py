# Задание №1
# Напишите функцию для поиска среднего значения в списке чисел и соответствующие юниттесты с использованием фреймворка pytest.

def average(lst: list[int | float]) -> float:
    for item in lst:
        if not isinstance(item, (int, float)):
            raise ValueError(f'Item is not instance of int or float')
    if len(lst):
        return sum(lst) / len(lst)
    return 0.0


if __name__ == '__main__':
    lst = [1, 2, 3, 4 ,5]
    print(average(lst))