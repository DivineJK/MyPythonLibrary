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
