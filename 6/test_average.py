import pytest

from average import average


def test_average():
    lst = [1, 2, 3, 4, 5]
    assert average(lst) == 3.0, 'test_average failed'

def test_empty_average():
    assert average([]) == 0.0, 'test empty_average failed'
    
def test_not_int_float():
    lst = [1, 2, 3, 4, 'a']
    with pytest.raises(ValueError):
        assert average(lst)
        
def test_average_one_num():
    lst = [1]
    assert average(lst) == 1.0, 'test with one num failed'


if __name__ == '__main__':
    pytest.main(['-v'])