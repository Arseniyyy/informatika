# 7830
from itertools import product, permutations

def f(x, y, z, w):
    return not y and (x <= ((not z) == w)) or z

for vector in product([0, 1], repeat=4):
    a, b, c, d = vector
    table = [(0, a, 0, 0),
             (b, 0, 1, 0),
             (c, 0, 0, d),]
    if len(set(table)) == len(table):
        for letter_tuple in permutations('xywz'):
            if all(f(**dict(zip(letter_tuple, row))) == 0 for row in table):
                print(*letter_tuple, sep='')
