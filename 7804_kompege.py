# 7804
from itertools import product, permutations

def f(x, y, z, w):
    return not y and (x <= ((not z) == w)) or z

for vector in product([0, 1], repeat=6):
    a, b, c, d, e, f = vector
    table = [(a, b, c, 0),
             (0, d, e, 0),
             (0, f, 0, 0),]
    if len(set(table)) == len(table):
        for letter_tuple in permutations('xywz'):
            if all(f(**dict(zip(letter_tuple, row))) == 0 for row in table):
                print(*letter_tuple, sep='')

