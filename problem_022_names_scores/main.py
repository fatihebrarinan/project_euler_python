# https://projecteuler.net/problem=22

FILE_NAME = "0022_names.txt"

with open(FILE_NAME, "r") as file:
    names = file.read().replace('"', '').lower().split(",")
names.sort()

# summation_of_scores = 0
# for index, name in enumerate(names, start=1):
#     alphabetical_value = sum((ord(char) - 96) for char in name)
#     score = alphabetical_value * index
#     summation_of_scores += score

summation_of_scores = sum((sum((ord(char) - 96) for char in name) * index) for index, name in enumerate(names, start=1))
print(summation_of_scores)