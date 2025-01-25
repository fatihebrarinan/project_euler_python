# https://projecteuler.net/problem=4

num1 = 999
num2 = 999
largest_palindrome = 0
while num1 > 0:
    num2 = 999
    while num2 > 0:
        if str(num1 * num2) == str(num1 * num2)[::-1]:
            if num1*num2 > largest_palindrome:
                largest_palindrome = num1 * num2
                print(f"{num1}, {num2}")
        num2 -= 1
    num1 -= 1
print(largest_palindrome)

