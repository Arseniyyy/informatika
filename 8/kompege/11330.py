# -*- coding: utf-8 -*-

abc = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'[::-1]
w = 'ИНФОРМАТИКА'
c = [abc.index(x) for x in w]
def cc(n, base):
    return sum(v * base ** k for k, v in enumerate(n[::-1]))

print(cc(c, 33) + 1)
