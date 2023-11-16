from math import gcd


def f(start_number, end_number):
    # +1, +3, +7
    # 13 -> 31
    if start_number > end_number:
        return 0
    if start_number == end_number:
        return 1
    if gcd(start_number, start_number + 1) == 1 and gcd(start_number + 3, start_number) == 1 and gcd(start_number + 7, start_number) == 1:
        return f(start_number + 1, end_number) + f(start_number + 3, end_number) + f(start_number + 7, end_number)
    return 0


print(f(13, 31))

