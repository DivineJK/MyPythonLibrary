import sys
input = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
def solveDiscreteLogarithm(x, y, m):
    if y >= m or y < 0:
        return -1
    if x == 0:
        if m == 1:
            return 0
        if y == 1:
            return 0
        if y == 0:
            return 1
        return -1
    # factorization of x
    p = 3
    tmp = x - 1
    cnt = 0
    primes = []
    counts = []
    ps = 0
    while tmp & 1:
        tmp >>= 1
        cnt += 1
    if cnt:
        primes.append(2)
        counts.append(cnt)
        ps += 1
    tmp += 1
    while tmp != 1:
        cnt = 0
        while tmp % p == 0:
            tmp //= p
            cnt += 1
        if cnt:
            primes.append(p)
            counts.append(cnt)
            ps += 1
        p += 2
        if tmp != 1 and p * p > x:
            primes.append(tmp)
            counts.append(1)
            ps += 1
            break
    # get length of tail
    tail = 0
    mp = m
    for i in range(ps):
        f = 0
        while mp % primes[i] == 0:
            mp //= primes[i]
            f += 1
        if tail < (f + counts[i] - 1) // counts[i]:
            tail = (f + counts[i] - 1) // counts[i]
    # check solution exists in tail
    z = 1
    for i in range(tail):
        if z == y:
            return i
        z = z * x % m
    # if y = 0 mod gcd(z, m), there's no solution
    if y % gcd(z, m):
        return -1
    # calculate totient(mp)
    p = 3
    u = mp
    tmp = mp - 1
    if tmp & 1:
        u >>= 1
        while tmp & 1:
            tmp >>= 1
    tmp += 1
    while tmp != 1:
        if tmp % p == 0:
            u //= p
            u *= p - 1
            while tmp % p == 0:
                tmp //= p
        p += 2
        if tmp != 1 and p * p > mp:
            u //= tmp
            u *= tmp - 1
            break
    # get size of loop
    p = 1
    loop = u
    while p * p <= u:
        if u % p == 0:
            if z * pow(x, p, m) % m == z:
                loop = p
                break
            ip = u // p
            if z * pow(x, ip, m) % m == z:
                loop = ip
        p += 1
    # get ceil(sqrt(loop))
    l, r = 0, loop+1
    sq = (loop+1) >> 1
    while r - l > 1:
        if sq * sq <= loop:
            l = sq
        else:
            r = sq
        sq = (l + r) >> 1
    if sq * sq < loop:
        sq += 1
    # identity
    e = pow(x, loop, m)
    # inverse
    b = pow(pow(x, loop-1, m), sq, m)
    d = {}
    f = z
    for i in range(sq):
        d[f] = i
        f = f * x % m
    # baby-step-giant-step algorithm
    g = y
    for i in range(sq):
        if g in d:
            return i*sq+d[g]+tail
        g = g * b % m
    return -1
