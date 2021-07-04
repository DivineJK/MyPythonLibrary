def fzt1(f, modulo=0):
    n = len(f)
    bin_top = 1
    depth = 0
    while bin_top < n:
        depth += 1
        bin_top <<= 1
    res = [0]*bin_top
    for i in range(n):
        res[i] = f[i]
    for i in range(depth):
        offset = 1 << (i+1)
        for j in range(0, bin_top, offset):
            for k in range(1<<i):
                res[j+k] += res[j+k+(1<<i)]
                if modulo:
                    if res[j+k] >= modulo:
                        res[j+k] -= modulo
    return res
def fmt1(f, modulo=0):
    n = len(f)
    bin_top = 1
    depth = 0
    while bin_top < n:
        depth += 1
        bin_top <<= 1
    res = [0]*bin_top
    for i in range(n):
        res[i] = f[i]
    for i in range(depth):
        offset = 1 << (i+1)
        for j in range(0, bin_top, offset):
            for k in range(1<<i):
                res[j+k] -= res[j+k+(1<<i)]
                if modulo:
                    if res[j+k] < 0:
                        res[j+k] += modulo
    return res
def convolution_and(f, g, modulo=0):
    n, m = len(f), len(g)
    S = max(n, m)
    flg = False
    while S & (S - 1):
        S = S & (S - 1)
        flg = True
    if flg:
        S <<= 1
    x = [0]*S
    y = [0]*S
    for i in range(n):
        x[i] = f[i]
    for i in range(m):
        y[i] = g[i]
    x = fzt1(x, modulo)
    y = fzt1(y, modulo)
    for i in range(S):
        x[i] *= y[i]
        if modulo:
            x[i] %= modulo
    x = fmt1(x, modulo)
    return x
