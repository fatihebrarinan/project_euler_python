# https://projecteuler.net/problem=25

number1 = 1
number2 = 1
index = 2
while len(str(number2)) < 1000:
    pre_number1 = number1
    number1 = number2
    number2 = pre_number1 + number2
    index += 1

print(index)


