def differentiate(f, MOD=MOD_free):
    n = len(f)
    res = [0]*n
    for i in range(1, n):
        res[i-1] = i * f[i] % MOD
    return res
