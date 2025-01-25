# https://projecteuler.net/problem=3
NUM = 600851475143

num = 2
while num < NUM:
    if NUM % num == 0:
        NUM = NUM / num
        num = 1
        result = NUM
    num += 1
print(result)

