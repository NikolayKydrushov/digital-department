
# Задание №5.
# Последовательно вводятся ненулевые числа. Определить сумму положительных и сумму отрицательных чисел. Закончить ввод чисел при вводе 0.

positive = 0
negative = 0

while True:
    number = int(input("Введите число: "))

    if number == 0: break
    elif number > 0: positive += number
    else: negative += number

print(f"Сумма положительных чисел = {positive} \nСумма отрицательных чисел = {negative}")