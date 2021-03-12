# sum(r^i*i^d for i=0..infinity) mod modulo

def unnamed_series(r, d, modulo):
    if r % modulo == 1: return -1
    res = 0
    fact = [1]*(d+2)
    invf = [1]*(d+2)
    invr = [1]*(d+2)
    for i in range(d+1):
        fact[i+1] = (i + 1) * fact[i] % modulo
        invr[d-i] = invr[d+1-i] * (modulo-r) % modulo
    x, y, u, v, k, l = 1, 0, 0, 1, fact[-1], modulo
    while l:
        x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
    invf[-1] = x % modulo
    for i in range(d+1, 0, -1):
        invf[i-1] = i * invf[i] % modulo
    bas = 1
    tmp = bas * pow(0, d, modulo) % modulo
    for i in range(d+2):
        res += (tmp * invr[i] % modulo) * (invf[i] * invf[d+1-i] % modulo) % modulo
        if res >= modulo: res -= modulo
        bas = bas * r % modulo
        tmp += bas * pow(i+1, d, modulo) % modulo
        if tmp >= modulo: tmp -= modulo
    x, y, u, v, k, l = 1, 0, 0, 1, (modulo+1-r)%modulo, modulo
    while l:
        x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
    return res * fact[d+1] * pow(x, d+1, modulo) % modulo
