# -*- coding: utf-8 -*-
from itertools import product


def f():
    alphabet = 'абвгд'
    comb = 'эюя'
    c = 0
    for t in product(comb, alphabet, alphabet, alphabet, comb):
        c += 1
    return c


print(f())

