from itertools import combinations, permutations, product


def f():
    alphabet = 'abc'
    alphabet_with_x = 'abcx'
    c = 0
    for t in product(alphabet, alphabet, alphabet, alphabet, alphabet_with_x):
        c += 1
    return c

print(f())

