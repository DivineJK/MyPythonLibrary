def differentiate(f, modulo):
    n = len(f)
    res = [0]*n
    for i in range(1, n):
        res[i-1] = i * f[i] % modulo
    return res
