# https://projecteuler.net/problem=24

from itertools import permutations

perm = permutations([0,1,2,3,4,5,6,7,8,9])
result = list(perm)[999999]
print(result)
