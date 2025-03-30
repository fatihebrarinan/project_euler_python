# https://projecteuler.net/problem=33
from fractions import Fraction


def has_crossed_same_digit(num1, num2): #ab,bc or ba,cb.
    str_num1 = str(num1)
    str_num2 = str(num2)
    if num1 == num2:
        return False
    if str_num1[0] == str_num2[1] and int(str_num2[0]) != 0:
        return int(str_num1[1]) / int(str_num2[0]) == num1 / num2
    elif str_num1[1] == str_num2[0] and int(str_num2[1]) != 0:
        return int(str_num1[0]) / int(str_num2[1]) == num1 / num2
    else:
        return False

multiplication = 1

for numerator in range(10,100):
    for denominator in range(numerator + 1,100):
        if has_crossed_same_digit(numerator, denominator):
            multiplication *= (numerator/denominator)

print(Fraction(multiplication).limit_denominator().denominator)






