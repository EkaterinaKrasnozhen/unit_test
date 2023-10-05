from random import randint


def get_randomList(size: int) ->list[int]:
    return [randint(0, 100) for _ in range(size)]