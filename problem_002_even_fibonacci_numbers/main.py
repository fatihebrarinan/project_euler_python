# https://projecteuler.net/problem=2
sum = 0
first = 1
second = 1
while second < 4000000:
    new_second = first + second
    first = second
    second = new_second
    if second % 2 == 0:
        sum += second
print(sum)
