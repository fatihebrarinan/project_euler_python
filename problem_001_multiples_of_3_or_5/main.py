# https://projecteuler.net/problem=1
result = sum(num for num in range(1000) if num % 3 == 0 or num % 5 == 0)
print(result)
