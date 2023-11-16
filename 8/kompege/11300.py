from itertools import product


def main():
    alphabet = 'бгдноуш'
    b_letter = 'б'
    n_letter = 'н'
    u_letter = 'у'
    indexes_list = []

    for index, t in enumerate(product(alphabet, repeat=6)):
        if (index + 1) % 2 != 0 and t[0] != b_letter and t.count(n_letter) >= 2 and t.count(u_letter) == 0:
            indexes_list.append(index + 1)
    return max(indexes_list)

print(main())

