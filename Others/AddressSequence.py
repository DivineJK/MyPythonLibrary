def makeAddressSequence(n, m):
    t = 1
    l = 0
    while n >= t:
        n -= t
        t *= m
        l += 1
    v = [0]*l
    for i in range(l):
        v[i] = n % m
        n //= m
    return v
def transformSequenceToString(n):
    v = makeAddressSequence(n, 26)
    n = len(v)
    S = ""
    for i in range(n, 0, -1):
        S = S[:] + chr(v[i-1]+ord('a'))
    return S
