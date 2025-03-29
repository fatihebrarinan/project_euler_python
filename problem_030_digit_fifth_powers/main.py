# https://projecteuler.net/problem=30
from itertools import product

# Starting from 2 since 1 doesn't count. Also, after 1 million, the condition is never true.
result_list = []
for repeat in range(1,7):
    for tup in product(range(10), repeat=repeat):
        sum_of_fifth_power = 0
        number_str = ""
        for num in tup:
            sum_of_fifth_power += pow(num, 5)
            number_str += str(num)
        number = int(number_str)
        if number == sum_of_fifth_power and number not in result_list:
            result_list.append(number)

result_list.remove(1) #Since 1 is not a sum, we remove it.
print(sum(result_list))








