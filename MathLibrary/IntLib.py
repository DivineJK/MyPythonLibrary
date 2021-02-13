def gcd(a, b):
    while b:
        a, b = b, a % b
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
    if b < 0:
        a, b, c = -a, -b, -c
    tk, tl = a, b
    while tl:
        tk, tl = tl, tk % tl
    if c % tk:
        return -1, -1
    a //= tk
    b //= tk
    c //= tk
    x, y, u, v, k, l = 1, 0, 0, 1, a, b
    while l:
        x, y, u, v = u, v, x - u * (k // l), y - v * (k // l)
        k, l = l, k % l
    x = c*x % b
    y = (c-a*x)//b
    return x, y
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
    c = 1
    while p * p <= n:
        if n % p == 0:
            c += 1
            L.append(p)
        p += 1
    for i in range(c, 0, -1):
        if L[i-1] * L[i-1] != n:
            L.append(n // L[i-1])
    return L
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
def rep_unit(p, l, modulo=0):
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
