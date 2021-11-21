def factorization(n):
    a = n
    D = []
    p = 2
    cnt = 0
    while a % p == 0:
        a //= p
        cnt += 1
    if cnt:
        D.append((p, cnt))
    p += 1
    while a != 1:
        cnt = 0
        while a % p == 0:
            cnt += 1
            a //= p
        if cnt:
            D.append((p, cnt))
        p += 2
        if p * p > n and a != 1:
            D.append((a, 1))
            break
    return D
def factorization_divisors(d, limit=-1, is_sort=True, rev=False):
    res = [1]
    cnt = 1
    pnt = 0
    for i in d:
        tmp = i
        lgt = cnt
        for j in range(d[i]):
            for k in range(lgt):
                if limit == -1 or res[k]*tmp <= limit:
                    res.append(res[k]*tmp)
                    cnt += 1
            tmp *= i
    if is_sort: res.sort(reverse=rev)
    return res
