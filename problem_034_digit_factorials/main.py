# https://projecteuler.net/problem=34

import math

factorials = [math.factorial(d) for d in range(10)]

# Calculate the upper bound: 7 * 9! =  2,540,160
upper_bound = 7 * factorials[9]

result = 0

# Iterate through all numbers from 3 to not count 1 and 2 since they are not sums.
for num in range(3, upper_bound + 1):
    # Convert the number to a string to process each digit
    digit_sum = sum(factorials[int(d)] for d in str(num))
    if digit_sum == num:
        result += num

print(result)