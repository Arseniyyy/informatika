# -*- coding: utf-8 -*-
from itertools import product, permutations


def f():
    # 8098 решу егэ
    alphabet = 'лон'
    letter = 'с'
    c = 0

    # for _ in product(letter, alphabet, alphabet, alphabet, alphabet):
    #     print(_)
    #     c += 1
    # print(c)

    for t in product('слон', repeat=5):
        if t.count(letter) == 1:
            c += 1
    return c


print(f())


