def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if (n^1)&1:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True
def getPrimitiveRoot(bc, p):
    invb = 1
    while True:
        f = True
        t = invb
        for i in range(bc):
            if t == 1:
                f = False
                break
            t = (t * t) % p
        if t != 1:
            f = False
        if f:
            return (p, pow(invb, p-2, p), invb)
        invb += 1
def primitiveRootGeneratorInfinity(bc, count):
    c = 0
    L = []
    t = (1 << bc) + 1
    while c < count:
        if isPrime(t):
            L.append(getPrimitiveRoot(bc, t))
            c += 1
        t += 1 << (bc + 1)
    return L
def primitiveRootGeneratorLimited(bc, count, limit):
    c = 0
    L = []
    t = (1 << bc) + 1
    while c < count and t <= limit:
        if isPrime(t):
            L.append(getPrimitiveRoot(bc, t))
            c += 1
        t += 1 << (bc + 1)
    return L
def primitiveRootGenerator(bc, count, limit = -1):
    if limit == -1:
        return primitiveRootGeneratorInfinity(bc, count)
    return primitiveRootGeneratorLimited(bc, count, limit)

b = 26
L = primitiveRootGenerator(b, 10)
print("# primitive root: {}".format(b))
print()
print("|Prime Number|Primitive Root|Inverse Primitive Root|")
print("|:-:|:-:|:-:|")
for i in L:
    print("|{}|{}|{}|".format(i[0], i[1], i[2]))
