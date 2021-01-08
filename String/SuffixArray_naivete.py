def naivete(s):
    t = s[:]
    n = len(t)
    F = {}
    tmp = "!"
    F[tmp] = n-1
    for i in range(n, 1, -1):
        tmp = t[i-2] + tmp[:]
        F[tmp] = i - 2
    L = [(i, F[i]) for i in F]
    L.sort()
    res = [L[i][1] for i in range(n)]
    return res
