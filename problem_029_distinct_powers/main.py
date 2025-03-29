# https://projecteuler.net/problem=29

num_set = {pow(a,b) for b in range(2,101) for a in range(2,101)}
print(len(num_set))
