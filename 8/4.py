# -*- coding: utf-8 -*-
from itertools import product


def f():
    alphabet = 'абвгдэюя'
    comb = 'эюя'
    c = 0
    for item in product(comb, alphabet, alphabet, alphabet, alphabet):
        if any(char == item[-1] for char in comb):
            if not any(char in item[1:-1] for char in comb):
                c += 1
    return c


print(f())

