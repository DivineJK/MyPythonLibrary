import cmath
exp = cmath.exp
pi = 3.14159265358979323846264338
def simply_fft(f, inverse=False):
    n = len(f)
    if n == 0:
        raise RuntimeError("LIST OF LENGTH ZERO IS INVALID.") from None
    depth = 0
    bin_top = 1
    while bin_top < n:
        bin_top <<= 1
        depth += 1
    res = [0]*bin_top
    pos = 0
    for i in range(n-1):
        res[i] = f[pos]
        pos ^= (n - (1 << (depth - ((i+1)&-(i+1)).bit_length())))
    res[n-1] = f[pos]
    left = 2
    for i in range(depth):
        grow = 1
        seed = 0
        if inverse:
            seed = exp(2j*pi/left)
        else:
            seed = exp(-2j*pi/left)
        offset = 1 << i
        for k in range(offset):
            for j in range(k, n, 1<<(i+1)):
                u = res[j]
                v = res[j+offset] * grow
                res[j] = u + v
                res[j+offset] = u - v
            grow *= seed
        left <<= 1
    if inverse:
        for i in range(bin_top):
            res[i] /= bin_top
    return res

def bluestein_fft(f, inverse=False):
    n = len(f)
    bin_top = 1
    while bin_top < 2*n+1:
        bin_top <<= 1
    a = [0]*bin_top
    b = [0]*bin_top
    c = [0]*bin_top
    for i in range(2*n-1):
        if inverse:
            b[i] = exp(-1j*pi*(i-n+1)*(i-n+1)/n)
            c[i] = exp(1j*pi*(i-n+1)*(i-n+1)/n)
        else:
            b[i] = exp(1j*pi*(i-n+1)*(i-n+1)/n)
            c[i] = exp(-1j*pi*(i-n+1)*(i-n+1)/n)
    Y = simply_fft(b)
    for i in range(n):
        a[i] = f[i]*c[n+i-1]
    X = simply_fft(a)
    Z = [X[i]*Y[i] for i in range(bin_top)]
    Z = simply_fft(Z, True)
    res = [Z[i+n-1] for i in range(n)]
    for i in range(n):
        res[i] *= c[i+n-1]
    if inverse:
        for i in range(n):
            res[i] /= n
    return res
