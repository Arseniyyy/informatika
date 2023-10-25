from itertools import combinations, permutations, product

def f():
    letter = 'x'
    alphabet = 'abcx'
    ar = product(alphabet, repeat=5)
    
    counter = 0
    last_x_counter = 0
    for item in list(ar):
        last_character = item[-1]
        if last_character is letter and (item[0] != letter and item[1] != letter and item[2] != letter and item[3] != letter):
            last_x_counter += 1
        if letter not in item:
            counter += 1
    return counter + last_x_counter
        
print(f())
