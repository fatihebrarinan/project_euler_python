# https://projecteuler.net/problem=12
NUM = 500

is_on = True
number =0
sum = 0
while is_on:
    divisors = 0
    sum += number

    i = 1
    bound = sum
    while i < bound:
        if sum % i == 0:
            bound = sum / i
            divisors += 2
        i += 1

    if divisors > NUM:
        is_on = False
        print(sum)

    number += 1

# One flow of this algorithm is it cannot correctly find the number of factors of a square number.
# For example, according to the program 36 has 10 factors.

















# The method below is way too slow.
# is_on = True
# number = 0
# sum = 0
# while is_on:
#     sum += number
#
#     primes = []
#     sieve = set(range(2, sum + 1))
#     while sieve:
#         prime_num = min(sieve)
#         primes.append(prime_num)
#         sieve -= set(range(prime_num, sum + 1, prime_num))
#     multiply = 1
#     duplicate_sum = sum
#     for prime in primes:
#         counter = 0
#         while duplicate_sum % prime == 0:
#             duplicate_sum = duplicate_sum / prime
#             counter += 1
#         multiply *= (counter + 1)
#     if multiply > NUM:
#         is_on = False
#         print(sum)
#     number += 1

