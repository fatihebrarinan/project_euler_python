# https://projecteuler.net/problem=9

c = 0
is_on = True
while is_on:
    for b in range(1, c):
        for a in range(1,b):
            if a + b + c == 1000 and a**2 + b**2 == c **2:
                is_on = False
                result = a*b*c
    c += 1
print(result)