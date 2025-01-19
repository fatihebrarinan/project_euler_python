# https://projecteuler.net/problem=6
NUM = 100
sum_of_the_square = 0
square_of_sum = 0
for number in range(1, NUM + 1):
    sum_of_the_square += number **2
    square_of_sum += number
square_of_sum = square_of_sum ** 2
print(square_of_sum - sum_of_the_square)
