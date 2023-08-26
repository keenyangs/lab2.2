#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Программа для нахождения наибольшего и наименьшего числа из трех

# Запрос ввода трех чисел через запятую
a, b, c = map(int, input("Введите три числа через запятую: ").split(","))

# Нахождение наибольшего числа
if a >= b and a >= c:
    max_number = a
elif b >= a and b >= c:
    max_number = b
else:
    max_number = c

# Нахождение наименьшего числа
if a <= b and a <= c:
    min_number = a
elif b <= a and b <= c:
    min_number = b
else:
    min_number = c

# Вывод результатов на экран
print("Наибольшее число:", max_number)
print("Наименьшее число:", min_number)