# Задание №4
# Разработайте метод luckySum и напишите для него тесты. Этот метод принимает на вход три числа и возвращает
# их сумму. Однако, если одно из чисел равно 13, то оно не учитывается при подсчете суммы.
# Так, например, если b равно 13, то считается сумма только a и c.


def lucky_sum(num1: int, num2:int, num3: int) -> int:
    if num1 == num2 == num3 == 13:
        raise ValueError('Все числа равны 13')
    my_list = [num1, num2, num3]      
    return sum(filter(lambda x: x != 13, my_list))


if __name__ == '__main__':
    print(lucky_sum(13,13,13))
        
        
