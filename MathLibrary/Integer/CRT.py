def CRT(num, a_list, m_list):
    for i in range(num):
        x, y = extgcd(bas, -m_list[i], a_list[i]-r)
        if x < 0:
            return -1
        r += bas * x
        bas *= m_list[i]
    return r % bas
def garner(a, m, mod = 0):
    n = len(a)
    c = [0]*n
    b = 1
    res = 0
    for i in range(n):
        t = a[i]
        if a[i] >= m[i]:
            a[i] %= m[i]
        for j in range(i):
            t -= c[j]
            t = (t * single_modinv(m[j], m[i])) % m[i]
        res += b * t
        b *= m[i]
        c[i] = t
        if mod:
            res %= mod
            b %= mod
    return res
