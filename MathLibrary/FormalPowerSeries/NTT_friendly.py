# mod = 998244353, root = 31, inverse_root = 128805723
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
