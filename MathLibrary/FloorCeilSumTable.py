def getFloorCeilSumTable(n):
    flgs = [1]*(n+1)
    flgs[0] = 0
    flgs[1] = 0
    p = 3
    while p*p<=n:
        if flgs[p]:
            for i in range(p*p, n+1, p):
                flgs[i] = 0
        p += 2
    primes = []
    if n >= 2:
        primes.append(2)
        for i in range(3, n+1, 2):
            if flgs[i]:
                primes.append(i)
    d = [1]*(n+1)
    d[0] = 0
    for i, k in enumerate(primes):
        t = 1
        u = k
        while u <= n:
            d[u] += d[t]
            t += 1
            u += k
    for i in range(n):
        d[i+1] += d[i]
    res = [0]*(n+1)
    for i in range(n):
        res[i+1] = res[i] + 2*i+1 + d[i+1] + d[i]
    return res
