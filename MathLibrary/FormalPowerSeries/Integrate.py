def integrate(f, modulo):
    n = len(f)
    if n == 1:
        return [0]
    res = [0]*n
    invn = [1, 1]
    res[1] = f[0]
    for i in range(2, n):
        invn.append((modulo-1)*invn[modulo%i]%modulo)
        invn[i] *= modulo // i
        invn[i] %= modulo
        res[i] = f[i-1] * invn[i] % modulo
    return res
