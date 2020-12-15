def primes(n):
    flg = [True]*(n+1)
    flg[0] = False
    flg[1] = False
    p = 2
    while p * p <= n:
        if flg[p]:
            for i in range(p, n//p+1):
                flg[p*i] = False
        p += 1
    res = []
    for i in range(n+1):
        if flg[i]:
            res.append(i)
    return res
