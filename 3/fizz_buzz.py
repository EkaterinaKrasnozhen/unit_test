# Задание №1
# Создайте набор тестов, полностью покрывающих все ветви кода функции fizzBuzz. Эта
# функция принимает на вход число и возвращает "Fizz", если число делится на 3, "Buzz",
# если число делится на 5, и "FizzBuzz", если число делится на 15. Если число не делится ни
# на 3, ни на 5, ни на 15, функция возвращает входное число в виде строки.

def fizz_buzz(num: int) -> str:
    assert type(num) == int, 'необходимо ввести целое число'
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    return str(num)


if __name__ == '__main__':
    print(fizz_buzz(25))