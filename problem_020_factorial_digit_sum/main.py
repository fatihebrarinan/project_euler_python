# https://projecteuler.net/problem=20

NUM = 100
factorial_num = 1
for number in range(NUM,0,-1):
    factorial_num *= number

sum_of_digits = 0
for digit in str(factorial_num):
    sum_of_digits += int(digit)
print(sum_of_digits)