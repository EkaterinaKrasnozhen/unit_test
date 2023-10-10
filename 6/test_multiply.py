# Задание №6
# Напишите функцию multiply(a, b), которая возвращает произведение a и b.
# Затем напишите параметризованный тест, который проверяет эту функцию на нескольких наборах данных.

import pytest
from multiply import multiply


@pytest.mark.parametrize('a, b, result', [
    (2, 2, 4),
    (3, 3, 9),
    (-2, 2, -4),
    (-2, -4, 8)
])
def test_multiply(a, b, result):
    assert multiply(a, b) == result, 'test multiply failed'


if __name__ == '__main__':
    pytest.main(['-v'])
