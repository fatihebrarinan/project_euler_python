# https://projecteuler.net/problem=5
NUM = 20
# Solve by human brain:

# it can be written as powers of prime numbers.
# 2,3,5,7,11,13,17,19 are the prime numbers.
# Largest power of 2 is 16. 3 is 9. rest is itself.
# Then the answer is:
result = 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19
print(result)

# Solve by program:
result = 1
for number in range(2,NUM + 1):
    multiplied_number = number
    while multiplied_number * number < NUM:
        multiplied_number *= number
    if result % multiplied_number != 0:
        result *= multiplied_number
print(result)