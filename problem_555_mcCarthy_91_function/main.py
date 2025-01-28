# https://projecteuler.net/problem=555

def m_function(m,k,s,n):
    while n <= m:
        while n <= m:
            n += k
        n -= s
    return n - s

    # while 0 <= n <= m:
    #     n = m_function(m, k, s, n + k)
    # return n - s

    # if n > m:
    #     return n - s
    # if 0 <= n <= m:
    #     return m_function(m,k,s,n = m_function(m,k,s,n = n+k))


def f_function(m,k,s):
    range_set = []
    for n in range(0,m + 1):
        if m_function(m,k,s,n) == n:
            range_set.append(n)
    return range_set


def sf_function(m,k,s):
    return sum(f_function(m,k,s))


def s_function(p,m):
    return sum(sf_function(m, k, s) for s in range(1, p) for k in range(s + 1, p + 1))

print(s_function(10**6,10**6))

# Works but way too slow. Will come back.