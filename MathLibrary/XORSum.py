def xorSum(f, modulo = 0):
    # calculate S = sum(f[i]^f[j] for 1 <= i < j <= n)
    # S = n * sum(f) - sum((1<<i)*(sum((f[k]>>i)&1)))**2
    # time: O(n*log(max(f)))
    S = 0
    n = len(f)
    mlg = 0
    g = max(f)
    while g:
        mlg += 1
        g >>= 1
    if modulo:
        y = [0]*mlg
        for i in range(n):
            S += f[i]
            if S >= mod:
                S -= mod
            for j in range(mlg):
                if (f[i] >> j) & 1:
                    y[j] += 1
                    if y[j] >= mod:
                        y[j] -= mod
        S = (n * S) % mod
        b = 1
        for i in range(mlg):
            S -= ((y[i] * y[i]) % mod) * b % mod
            if S < 0:
                S += mod
            b <<= 1
            b %= mod
        return S
    for i in range(n):
        S = (S + f[i]) % mod
        for j in range(mlg):
            if (f[i] >> j) & 1:
                y[j] += 1
    S *= n
    b = 1
    for i in range(mlg):
        S -= y[i] * y[i] * b
        b <<= 1
    return S
