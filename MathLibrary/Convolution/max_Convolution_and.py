def max_convolution_and(a, b):
    m = max(max(a), max(b))
    bt = 0
    while m:
        bt += 1
        m >>= 1
    n, m = len(a), len(b)
    val = 0
    c = [1]*n
    d = [1]*m
    for i in range(bt, 0, -1):
        bit = 1 << (i - 1)
        cnta, cntb = 0, 0
        for j in range(n):
            if c[j] and (a[j] & bit):
                cnta = 1
                break
        for j in range(m):
            if d[j] and (b[j] & bit):
                cntb = 1
                break
        if cnta and cntb:
            val += bit
            for j in range(n):
                if not (a[j] & bit):
                    c[j] = 0
            for j in range(m):
                if not (b[j] & bit):
                    d[j] = 0
    return val
