# https://projecteuler.net/problem=10
BOUND = 2000000

nums = set(range(2, BOUND + 1))
sum = 0
while nums:
    prime_number = min(nums)
    print(prime_number)
    sum += prime_number
    nums -= set(range(prime_number*prime_number, BOUND + 1, prime_number))
print(sum)

# Takes about 20 minutes.