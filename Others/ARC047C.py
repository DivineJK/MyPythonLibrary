def ARC047C(n, k):
    x = [0]*n
    t = n
    for i in range(n-k+1):
        x[i] = t // k
        t = (t % k) * (n - i - 1)
    p = n - k
    while x[p] == 0:
        x[p] = n - p - 1
        p -= 1
    x[p] -= 1
    for i in range(k-1):
        x[n-i-1] = i
    tree = [0]*(n+1)
    for i in range(n):
        p = i + 1
        while p <= n:
            tree[p] += 1
            p += p - (p & (p - 1))
    res = [0]*n
    for i in range(n):
        t = x[i]
        l, r = 0, n
        d = r // 2
        while r - l > 1:
            p = d
            s = 0
            while p:
                s += tree[p]
                p &= p - 1
            if s <= t:
                l = d
            else:
                r = d
            d = (l + r) // 2
        res[i] = d
        p = d + 1
        while p <= n:
            tree[p] -= 1
            p += p - (p & (p - 1))
    return res
