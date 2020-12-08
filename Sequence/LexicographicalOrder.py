def lexi_num(n, a, modulo=0):
    comp = sorted(a)
    D = {comp[i]: i+1 for i in range(n)}
    lexi = [D[a[i]] for i in range(n)]
    fact = [1]*n
    for i in range(n-1):
        fact[i+1] = fact[i] * (i + 1)
        if modulo:
            fact[i+1] %= modulo
    fenwick_tree = [0]*(n+1)
    for i in range(1, n+1):
        fenwick_tree[i] = i - (i & (i - 1))
    res = 1
    for i in range(n):
        x = lexi[i]
        while x <= n:
            fenwick_tree[x] -= 1
            x += x - (x & (x - 1))
        x = lexi[i]
        s = 0
        while x:
            s += fenwick_tree[x]
            x = x & (x - 1)
        res += s * fact[n-i-1]
        if modulo:
            res %= modulo
    return res
