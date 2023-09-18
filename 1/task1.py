from math import sqrt


def square_root(num: float) -> float:
    #assert num > 0, 'Число должно быть больше 0'
    if num < 0:
        raise RuntimeError(f' Число {num} должно быть больше 0')
    return sqrt(num)


def test_square_root_positive():
    assert square_root(25) == 5, 'Тест с положительными числами провален'


def test_square_root_zero():
    assert square_root(0) == 0, 'Тест с нулевыми значениями провален'
    
    
def test_square_root_negative():
    try:
        square_root(-5)
        #raise Exception('Ожидалась ошибка')
    except RuntimeError:
        print('Все тесты прошли')


if __name__ == '__main__':
    #print(square_root(-10))
    test_square_root_positive()
    test_square_root_zero()
    test_square_root_negative()