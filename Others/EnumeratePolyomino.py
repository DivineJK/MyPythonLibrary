def enumeratePolyomino(n):
    if n <= 0:
        return []
    if n == 1:
        return [[(0, 0)]]
    vec = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    F = [[], [[(0, 0)]]]
    for i in range(2, n+1):
        F.append([])
        for j in F[i-1]:
            L = []
            for k in j:
                for v in vec:
                    iv = (k[0]+v[0], k[1]+v[1])
                    if iv not in j and iv not in L:
                        L.append(iv)
            for k in L:
                u = [l for l in j] + [k]
                mx, my = n + 13, n + 13
                for l in u:
                    if mx > l[0]:
                        mx = l[0]
                    if my > l[1]:
                        my = l[1]
                u2 = [(l[0]-mx, l[1]-my) for l in u]
                u2.sort()
                if u2 not in F[i]:
                    F[i].append(u2)
    return F[n]
