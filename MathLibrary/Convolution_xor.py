def conv_xor(n, f, g):
    if n == 1:
        return [f[0]*g[0]%mod]
    f0 = [f[i] for i in range(n//2)]
    f1 = [f[i] for i in range(n//2, n)]
    g0 = [g[i] for i in range(n//2)]
    g1 = [g[i] for i in range(n//2, n)]
    x00 = conv_xor(n//2, f0, g0)
    x01 = conv_xor(n//2, f0, g1)
    x10 = conv_xor(n//2, f1, g0)
    x11 = conv_xor(n//2, f1, g1)
    return [(x00[i]+x11[i])%mod for i in range(n//2)] + [(x01[i]+x10[i])%mod for i in range(n//2)]
