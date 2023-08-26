#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Программа для вывода фразы "Мне n лет" с правильным склонением слова "лет"

n = int(input("Введите ваш возраст (натуральное число больше 100): "))

last_digit = n % 10

if last_digit == 1:
    print("Мне", n, "год.")
elif last_digit in [2, 3, 4]:
    print("Мне", n, "года.")
else:
    print("Мне", n, "лет.")