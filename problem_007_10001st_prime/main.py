# https://projecteuler.net/problem=7

NUM = 10001
prime_list = []
prime_num = 2
while len(prime_list) < NUM:
    is_prime = True
    for number in range(1, prime_num):
        if number != 1 and prime_num % number == 0:
            is_prime = False
            break
    if is_prime:
        prime_list.append(prime_num)
    prime_num += 1
print(prime_list[NUM - 1])

# Took around 1 minute.

