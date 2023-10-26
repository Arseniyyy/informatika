# -*- coding: utf-8 -*-
from itertools import product


def f():
    # 13486
    alphabet = 'пир'
    letter = 'п'
    c = 0

    for t in product(alphabet, repeat=5):
        if t.count(letter) == 1:
            c += 1
    return c


# f()
print(f())

