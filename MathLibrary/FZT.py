def FZT(f):
    n = len(f)
    if n <= 1:
        return f
    flg = [True]*(n+1)
    p = 3
    while p * p <= n:
        if flg[p]:
            for i in range(p*p, n+1, p<<1):
                flg[i] = False
        p += 2
    primes = [2]
    for i in range(3, n+1, 2):
        if flg[i]:
            primes.append(i)
    g = [f[i] for i in range(n)]
    for i in primes:
        t = 0
        for j in range(i, n+1, i):
            g[j-1] += g[t]
            t += 1
    return g
