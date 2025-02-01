# https://projecteuler.net/problem=23
from functools import reduce
LIMIT = 28123

num_list = [number for number in range(1,LIMIT + 1)]

def is_abundant(number):
    factor_set =  set(reduce(
        list.__add__,
        ([i, number // i] for i in range(1, int(number ** 0.5) + 1) if number % i == 0)))
    if sum(factor_set - {number}) > number:
        return True
    else:
        return False

abundant_list = [number for number in num_list if is_abundant(number)]

abundant_sum = {n1 + n2 for n1 in abundant_list for n2 in abundant_list if n1 + n2 <= LIMIT}

print(sum(set(num_list) - set (abundant_sum)))