def single_modinv(n, m):
    res = 1
    p = n
    while p > 1:
        res = res * (m - (m // p)) % m
        p = m % p
    return res
