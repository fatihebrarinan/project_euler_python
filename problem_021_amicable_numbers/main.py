# https://projecteuler.net/problem=21

from functools import reduce
NUM = 10000

def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def d_function(number):
    return sum(factors(number) - {number})

amicable_nums = []
for i in range(2,NUM):
    if i not in amicable_nums:
        amicable_pair = d_function(i)
        if d_function(amicable_pair) == i and amicable_pair != i:
            amicable_nums.extend([i,amicable_pair])
result = sum(amicable_nums)
print(result)