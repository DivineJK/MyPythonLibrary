def inved(a, modulo):
    x, y, u, v, k, l = 1, 0, 0, 1, a, modulo
    while l:
        x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
    return x % modulo
def fht(f, n, MOD):
    if n == 1:
        return f
    depth = len(bin(n))-3
    res = [0]*n
    pos = 0
    for i in range(n):
        res[i] = f[pos]
        tmp = ((i+1)&-(i+1)) << 1
        pos ^= (n-1)&(n-n//tmp)
    left = 2
    right = 1
    thgir = n >> 1
    for i in range(depth):
        grow = 1
        for k in range(right):
            idx_l = k
            idx_r = k + right
            for j in range(thgir):
                u = res[idx_l]
                v = res[idx_r]
                res[idx_l] = (u + v) % MOD
                res[idx_r] = (u - v) % MOD
                idx_l += left
                idx_r += left
        left <<= 1
        right <<= 1
        thgir >>= 1
    return res
def xor_convolution(f, g, MOD):
    n = len(f)
    m = len(f)
    bin_top = 1
    while bin_top < max(n, m):
        bin_top <<= 1
    x = f[:] + [0]*(bin_top-n)
    y = g[:] + [0]*(bin_top-m)
    x = fht(x, bin_top, MOD)
    y = fht(y, bin_top, MOD)
    for i in range(bin_top):
        x[i] = x[i] * y[i] % MOD
    x = fht(x, bin_top, MOD)
    ib = inved(bin_top, MOD)
    for i in range(bin_top):
        x[i] = x[i] * ib % MOD
    return x
