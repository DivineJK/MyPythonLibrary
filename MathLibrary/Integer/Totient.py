def totient(n):
    a = n
    res = 1
    q = 1
    if a & 1 == 0:
        q *= 2
        while a & 1 == 0:
            a >>= 1
    p = 3
    while a != 1:
        if a % p == 0:
            q *= p
            res *= p - 1
            while a % p == 0:
                a //= p
        p += 2
        if p * p > n and a != 1:
            res *= a - 1
            q *= a
            break
    return res * n // q
