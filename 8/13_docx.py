# -*- coding: utf-8 -*-
from itertools import permutations


def f():
    c = 0
    alphabet = 'ассасин'
    for l in permutations(alphabet):
        c += 1
    return c


print(f())

