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
