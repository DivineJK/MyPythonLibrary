MOD_free = 998244353
root_free = 128805723
invr_free = 31
#print(*bit_inverter)
def ntt_free(f, n, root=root_free):
    if n == 1:
        return f
    MOD = MOD_free
    depth = len(bin(n))-3
    res = [0]*n
    pos = 0
    for i in range(n-1):
        res[i] = f[pos]
        pos ^= (n - (1 << (depth - ((i+1)&-(i+1)).bit_length())))
    res[n-1] = f[pos]
    base_list = [1]*24
    base_list[-1] = root
    for i in range(23, 0, -1):
        base_list[i-1] = base_list[i] * base_list[i] % MOD
    for i in range(depth):
        grow = 1
        seed = base_list[i+1]
        offset = 1 << i
        for k in range(offset):
            for j in range(k, n, 1<<(i+1)):
                u = res[j]
                v = res[j+offset] * grow % MOD
                res[j] = u + v
                if res[j] >= MOD: res[j] -= MOD
                res[j+offset] = u - v
                if res[j+offset] < MOD: res[j+offset] += MOD
            grow = grow * seed % MOD
    return res
def inverse_ntt_free(f, n):
    res = ntt_free(f, n, invr_free)
    MOD = MOD_free
    x, y, u, v, k, l = 1, 0, 0, 1, n, MOD
    while l:
        x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
    x %= MOD
    for i in range(n):
        res[i] *= x
        res[i] %= MOD
    return res
def convolute_one(f, g, MOD=MOD_free):
    n = len(f)
    m = len(g)
    bin_top = 1
    while bin_top < n + m:
        bin_top <<= 1
    if n * m <= 100000:
        res = [0]*bin_top
        for i in range(n):
            for j in range(m):
                res[i+j] += (f[i] * g[j]) % MOD
                res[i+j] %= MOD
        return res
    x = f[:] + [0]*(bin_top-n)
    y = g[:] + [0]*(bin_top-m)
    x = ntt_free(x, bin_top)
    y = ntt_free(y, bin_top)
    for i in range(bin_top):
        x[i] = x[i] * y[i] % MOD
    return inverse_ntt_free(x, bin_top)

def differentiate(f, MOD=MOD_free):
    n = len(f)
    res = [0]*n
    for i in range(1, n):
        res[i-1] = i * f[i] % MOD
    return res

def integrate(f, MOD=MOD_free):
    n = len(f)
    if n == 1:
        return [0]
    res = [0]*n
    invn = [1, 1]
    res[1] = f[0]
    for i in range(2, n):
        invn.append((MOD-1)*invn[MOD%i]%MOD)
        invn[i] = (invn[i] * (MOD // i)) % MOD
        res[i] = f[i-1] * invn[i] % MOD
    return res

def inverse(f, MOD=MOD_free):
    g = [0]
    x, y, u, v, k, l = 1, 0, 0, 1, f[0], MOD
    while l:
        x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
    g[0] = x % MOD
    n = len(f)
    bin_top = 1
    while bin_top < n:
        bin_top <<= 1
    t = f[:] + [0]*(bin_top-n)
    x = [f[0]]
    m = 1
    while m < n:
        for i in range(m):
            x.append(t[i+m])
        m <<= 1
        h = convolute_one(x, g)[:m]
        h[0] = (2 - h[0]) % MOD
        for i in range(1, m):
            h[i] = (MOD - h[i]) % MOD
        g = convolute_one(g, h)[:m]
    return g

def fps_logarithm(f, MOD=MOD_free):
    n = len(f)
    bin_top = 1
    while bin_top < n:
        bin_top <<= 1
    x = f[:] + [0]*(bin_top-n)
    df = differentiate(x, MOD)
    inv_f = inverse(x)
    x = convolute_one(df, inv_f)
    return integrate(x, MOD)

def fps_exponential(f, MOD=MOD_free):
    n = len(f)
    bin_top = 1
    while bin_top < n:
        bin_top <<= 1
    t = f[:] + [0]*(bin_top-n)
    g = [1]
    p = [1]
    m = 1
    while 2*m <= bin_top:
        h = convolute_one(p, g)[:m]
        h[0] = (2 - h[0]) % MOD
        for i in range(1, m):
            h[i] = (MOD-h[i])%MOD
        g = convolute_one(g, h)[:m]
        q = differentiate(t[:m])
        r = convolute_one(p, q)[:2*m-1]
        for i in range(1, m):
            r[i-1] = (i * p[i] % MOD - r[i-1]) % MOD
        for i in range(m, 2*m):
            r[i-1] = (MOD - r[i-1]) % MOD
        w = convolute_one(g, r)[:2*m]
        for i in range(m):
            w[i] += q[i]
            w[i] %= MOD
        w = integrate(w)
        for i in range(2*m):
            w[i] = (t[i] - w[i]) % MOD
        x = convolute_one(p, w)
        for i in range(m):
            p[i] += x[i]
            p[i] %= MOD
            p.append(x[i+m])
        m <<= 1
    return p
