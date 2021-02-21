# mod = 998244353, root = 31, inverse_root = 128805723
MOD_free = 998244353
root_free = 128805723
invr_free = 31
def ntt_free(f, n, root=root_free):
    if n == 1:
        return f
    MOD = MOD_free
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

def inved(a, modulo):
    x, y, u, v, k, l = 1, 0, 0, 1, a, modulo
    while l:
        x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
    return x%modulo

class polynomial_taylor_shift:
    def __init__(self):
        self.fact_cnt = 0
        self.fact = [1]
        self.invf = [1]
    def polynomial_taylor_shift(self, f, c, MOD=MOD_free):
        n = len(f)
        if n > self.fact_cnt:
            for i in range(self.fact_cnt, n):
                self.fact.append(self.fact[i]*(i+1)%MOD)
                self.invf.append(1)
            self.invf[-1] = inved(self.fact[-1], MOD)
            for i in range(n, self.fact_cnt, -1):
                self.invf[i-1] = self.invf[i] * i % MOD
            self.fact_cnt = n
        x = [0]*n
        y = [0]*n
        tmp = 1
        for i in range(n):
            x[n-i-1] = f[i] * self.fact[i] % MOD
            y[i] = tmp * self.invf[i] % MOD
            tmp = c * tmp % MOD
        x = convolute_one(x, y)[:n]
        for i in range(n//2):
            x[i], x[n-i-1] = x[n-i-1], x[i]
        for i in range(n):
            x[i] = x[i] * self.invf[i] % MOD
        return x
