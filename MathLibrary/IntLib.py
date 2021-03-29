def gcd(a, b):
    while b:
        a, b = b, a % b
    if a < 0: return -a
    return a
def extgcd(a, b, c):
    if b == 0:
        if a == 0:
            if c == 0:
                return 0, 0
            return -1, -1
        if c % a == 0:
            return c // a, 0
        return -1, -1
    x, y, u, v, k, l = 1, 0, 0, 1, a, b
    while l:
        x, y, u, v = u, v, x - u * (k // l), y - v * (k // l)
        k, l = l, k % l
    if k < 0: k = -k
    if c % k: return -1, -1
    a, b, c = a // k, b // k, c // k
    if b < 0: a, b, c = -a, -b, -c
    x *= c
    y *= c
    u = (b - x - 1) // b
    return x+u*b, y-u*a
def inved(a, modulo):
    x, y, u, v, k, l = 1, 0, 0, 1, a, modulo
    while l:
        x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
    return x%modulo
def CRT(num, a_list, m_list):
    for i in range(num):
        x, y = extgcd(bas, -m_list[i], a_list[i]-r)
        if x < 0:
            return -1
        r += bas * x
        bas *= m_list[i]
    return r % bas
def IsPrime(num):
    p = 2
    if num <= 1:
        return False
    while p * p <= num:
        if num % p == 0:
            return False
        p += 1
    return True
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
def totient(n):
    a = n
    p = 2
    res = n
    while a != 1:
        if a % p == 0:
            res //= p
            res *= p - 1
            while a % p == 0:
                a //= p
        p += 1
        if p * p > n and a != 1:
            res //= a
            res *= a - 1
            break
    return res
def repunit(p, l, modulo=0):
    res = 0
    bas = 1
    if modulo:
        bas = pow(10, p, modulo)
    else:
        bas = pow(10, p)
    rep_unit = 1
    while l:
        if l & 1:
            res *= bas
            res += rep_unit
            if modulo:
                res %= modulo
        rep_unit = (bas + 1) * rep_unit
        bas *= bas
        if modulo:
            rep_unit %= modulo
            bas %= modulo
        l >>= 1
    return res
