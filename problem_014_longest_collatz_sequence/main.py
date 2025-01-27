# https://projecteuler.net/problem=14

highest_step = 0
highest_step_number = 0
for i in range(1,1000001):
    number = i
    step = 0
    while number > 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1
        step += 1
    if step > highest_step:
        highest_step = step
        highest_step_number = i
print(highest_step_number)

