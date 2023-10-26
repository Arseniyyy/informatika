# -*- coding: utf-8 -*-
from itertools import permutations


def f():
    c = 0
    alphabet = 'пескарь'
    letter = 'ь'
    wrong_combinations = [letter + 'е',
                          letter + 'а',
                          letter + 'р']

    for l in permutations(alphabet):
        if l[0] != letter:
            if not any(i in ''.join(l) for i in wrong_combinations):
                c += 1
    return c

print(f())

