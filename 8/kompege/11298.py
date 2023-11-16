from itertools import product


def main():
    abc = 'бмнрю'
    index_list = []

    for index, t in enumerate(product(abc, repeat=6)):
        index += 1
        if index % 2 != 0 and t[0] != 'м' and t.count('р') >= 2 and t.count('ю') == 0:
            index_list.append(index)

    return max(index_list)

print(main())

