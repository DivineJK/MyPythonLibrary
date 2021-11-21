def eratosthenes(n):
    flg = [True]*(n+1)
    flg[0] = False
    flg[1] = False
    if n <= 1:
        return []
    p = 3
    while p * p <= n:
        if flg[p]:
            for i in range(p, n//p+1, 2):
                flg[p*i] = False
        p += 1
    res = [2]
    for i in range(3, n+1, 2):
        if flg[i]:
            res.append(i)
    return res