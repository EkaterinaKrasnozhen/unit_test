# Создайте тесты, обеспечивающие полное покрытие кода метода calculatingDiscount, который принимает сумму
# покупки и размер скидки, затем вычисляет и возвращает сумму с учетом скидки. Метод должен обрабатывать
# исключения, связанные с некорректным размером скидки или отрицательной суммой покупки.

TOTAL = 100


def calculate_discount(sum: float, discount: float) -> float:
        if discount < 0 or sum < 0:
            raise RuntimeError(f"Скидка должна быть больше 0")
        assert discount < 100, 'скидка должна быть в пределах от 0 до 100'
        res = sum - ((sum / TOTAL) * discount)
        return res
    
    
if __name__ == '__main__':
    print(calculate_discount(150, 105))