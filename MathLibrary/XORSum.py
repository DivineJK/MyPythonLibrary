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
    y = [0]*mlg
    if modulo:
        for i in range(n):
            S += f[i]
            if S >= modulo:
                S -= modulo
            for j in range(mlg):
                if (f[i] >> j) & 1:
                    y[j] += 1
                    if y[j] >= modulo:
                        y[j] -= modulo
        S = (n * S) % modulo
        b = 1
        for i in range(mlg):
            S -= ((y[i] * y[i]) % modulo) * b % modulo
            if S < 0:
                S += modulo
            b <<= 1
            b %= modulo
        return S
    for i in range(n):
        S += f[i]
        for j in range(mlg):
            if (f[i] >> j) & 1:
                y[j] += 1
    S *= n
    b = 1
    for i in range(mlg):
        S -= y[i] * y[i] * b
        b <<= 1
    return S
