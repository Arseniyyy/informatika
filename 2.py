from itertools import combinations, permutations, product


k = 0
for _ in product('км', 'уа', 'кума', 'кума', 'кума'):
    k += 1
print(k)
