def divisors(n):
    L = []
    p = 1
    c = 0
    while p * p <= n:
        if n % p == 0:
            c += 1
            L.append(p)
        p += 1
    for i in range(c, 0, -1):
        if L[i-1] * L[i-1] != n:
            L.append(n // L[i-1])
    return L
