# https://projecteuler.net/problem=19

#1 Jan 1900 is Monday.
#September, april, june and november have 30 days.
#February has 28, 29 on leap years.
month_day_list = [31,28,31,30,31,30,31,31,30,31,30,31]
day_counter = 2
result_counter = 0
def is_leap_year(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False

for i in range(0,1201):
    year = 1901 + int(i / 12)
    if is_leap_year(year) and i % 12 == 1:
        day_counter += 1

    if i > 11:
        i = i % 12

    day_counter += month_day_list[i]

    if day_counter % 7 == 0:
        result_counter += 1

print(result_counter)
