# mod = 377487361, root = 197, inverse_root = 3832359
def ntt1(f, n, root=3832359):
    if n == 1:
        return f
    MOD = 377487361
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
    base_list = [1]*24
    base_list[-1] = root
    for i in range(23, 0, -1):
        base_list[i-1] = base_list[i] * base_list[i] % MOD
    for i in range(depth):
        grow = 1
        seed = base_list[i+1]
        for k in range(right):
            idx_l = k
            idx_r = k + right
            for j in range(thgir):
                u = res[idx_l]
                v = res[idx_r] * grow % MOD
                res[idx_l] = (u + v) % MOD
                res[idx_r] = (u - v) % MOD
                idx_l += left
                idx_r += left
            grow = grow * seed % MOD
        left <<= 1
        right <<= 1
        thgir >>= 1
    return res
def inverse_ntt1(f, n):
    res = ntt1(f, n, 197)
    MOD = 377487361
    x, y, u, v, k, l = 1, 0, 0, 1, n, MOD
    while l:
        x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
    x %= MOD
    for i in range(n):
        res[i] *= x
        res[i] %= MOD
    return res
# mod = 595591169, root = 721, inverse_root = 72693513
def ntt2(f, n, root=72693513):
    if n == 1:
        return f
    MOD = 595591169
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
    base_list = [1]*24
    base_list[-1] = root
    for i in range(23, 0, -1):
        base_list[i-1] = base_list[i] * base_list[i] % MOD
    for i in range(depth):
        grow = 1
        seed = base_list[i+1]
        for k in range(right):
            idx_l = k
            idx_r = k + right
            for j in range(thgir):
                u = res[idx_l]
                v = res[idx_r] * grow % MOD
                res[idx_l] = (u + v) % MOD
                res[idx_r] = (u - v) % MOD
                idx_l += left
                idx_r += left
            grow = grow * seed % MOD
        left <<= 1
        right <<= 1
        thgir >>= 1
    return res
def inverse_ntt2(f, n):
    res = ntt2(f, n, 721)
    MOD = 595591169
    x, y, u, v, k, l = 1, 0, 0, 1, n, MOD
    while l:
        x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
    x %= MOD
    for i in range(n):
        res[i] *= x
        res[i] %= MOD
    return res
# mod = 645922817, root = 19, inverse_root = 135983751
def ntt3(f, n, root=135983751):
    if n == 1:
        return f
    MOD = 645922817
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
    base_list = [1]*24
    base_list[-1] = root
    for i in range(23, 0, -1):
        base_list[i-1] = base_list[i] * base_list[i] % MOD
    for i in range(depth):
        grow = 1
        seed = base_list[i+1]
        for k in range(right):
            idx_l = k
            idx_r = k + right
            for j in range(thgir):
                u = res[idx_l]
                v = res[idx_r] * grow % MOD
                res[idx_l] = (u + v) % MOD
                res[idx_r] = (u - v) % MOD
                idx_l += left
                idx_r += left
            grow = grow * seed % MOD
        left <<= 1
        right <<= 1
        thgir >>= 1
    return res
def inverse_ntt3(f, n):
    res = ntt3(f, n, 19)
    MOD = 645922817
    x, y, u, v, k, l = 1, 0, 0, 1, n, MOD
    while l:
        x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
    x %= MOD
    for i in range(n):
        res[i] = x * res[i] % MOD
    return res
def crt(a_list):
    m_list = (377487361, 595591169, 645922817)
    bas = 1
    r = 0
    for i in range(3):
        b = m_list[i]
        c = r-a_list[i]
        x, y, u, v, k, l = 1, 0, 0, 1, -bas, b
        while l:
            x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
        x = c*x % b
        y = (c+bas*x)//b
        if x < 0:
            return -1
        r += bas * x
        bas *= m_list[i]
    return r % bas
def convolute(f, g, modulo):
    n = len(f)
    m = len(g)
    bin_top = 1
    while bin_top < n + m:
        bin_top <<= 1
    if n * m <= 100000:
        res = [0]*bin_top
        for i in range(n):
            for j in range(m):
                res[i+j] += (f[i] * g[j]) % modulo
                res[i+j] %= modulo
        return res
    MOD1 = 377487361
    MOD2 = 595591169
    MOD3 = 645922817
    f = f[:] + [0]*(bin_top-n)
    g = g[:] + [0]*(bin_top-m)
    x = ntt1(f, bin_top)
    y = ntt1(g, bin_top)
    z1 = [x[i]*y[i]%MOD1 for i in range(bin_top)]
    z1 = inverse_ntt1(z1, bin_top)
    x = ntt2(f, bin_top)
    y = ntt2(g, bin_top)
    z2 = [x[i]*y[i]%MOD2 for i in range(bin_top)]
    z2 = inverse_ntt2(z2, bin_top)
    x = ntt3(f, bin_top)
    y = ntt3(g, bin_top)
    z3 = [x[i]*y[i]%MOD3 for i in range(bin_top)]
    z3 = inverse_ntt3(z3, bin_top)
    res = [crt((z1[i], z2[i], z3[i])) % modulo for i in range(bin_top)]
    return res
