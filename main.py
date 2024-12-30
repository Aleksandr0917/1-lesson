# Задача 1 (просто) "Арифметика"
# 1st program
result1 = 9 ** 0.5 * 5
print(result1)  # Ожидаемый результат: 15.0

# Задача 2 (просто) "Логика"
# 2nd program
result2 = (9.99 > 9.98) and (1000 != 1000.1)
print(result2)  # Ожидаемый результат: True

# Задача 3 (средне) "Школьная загадка"
# 3rd program
result3a = 2 * 2 + 2  # без приоритета
result3b = 2 * (2 + 2)  # с приоритетом для сложения
print(result3a)  # Ожидаемый результат: 6
print(result3b)  # Ожидаемый результат: 8
print(result3a == result3b)  # Ожидаемый результат: False

# Задача 4 (сложно) "Первый после точки"
# 4th program
number_str = '123.456'
number_float = float(number_str)  # Преобразуем строку в дробное число
shifted_number = number_float * 10  # Умножаем на 10
first_digit_after_decimal = int(shifted_number) % 10  # Находим первую цифру после запятой
print(first_digit_after_decimal)  # Ожидаемый результат: 4

