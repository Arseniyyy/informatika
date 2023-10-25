# -*- coding: utf-8 -*-
from itertools import product


def f():
    alphabet = 'зима'
    vowels = 'иа'
    consonants = 'зм'
    c = 0

    for i in product(consonants, alphabet, alphabet, alphabet, vowels):
        c += 1
    return c

print(f())

