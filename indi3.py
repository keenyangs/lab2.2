#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sum = 0
for n in range(1, 5):
    for i in range(10**(n-1), 10**n):
        sum += i
print(sum)