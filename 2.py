from itertools import combinations, permutations, product


k = 0
for _ in product('��', '��', '����', '����', '����'):
    k += 1
print(k)
