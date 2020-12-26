def inved(a):
    x, y, u, v, k, l = 1, 0, 0, 1, a, mod
    while l:
        x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
    return x % mod
def fht(f, n, inverse=False):
    if n == 1:
        return f
    if n == 2:
        ipl = inved(2)
        if inverse:
            return [ipl * (f[0] + f[1]) % mod, ipl * (f[0] - f[1]) % mod]
        return [(f[0] + f[1]) % mod, (f[0] - f[1]) % mod]
    f0 = [f[i] for i in range(n//2)]
    f1 = [f[i] for i in range(n//2, n)]
    x0 = fht(f0, n//2)
    x1 = fht(f1, n//2)
    x = [(x0[i]+x1[i]) % mod for i in range(n//2)] + [(x0[i]-x1[i]) % mod for i in range(n//2)]
    if inverse:
        ipl = inved(n)
        for i in range(n):
            x[i] *= ipl
            x[i] %= mod
    return x
