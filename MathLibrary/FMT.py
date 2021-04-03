def FMT(f):
    n = len(f)
    p_flg = [True]*(n+1)
    p_flg[0] = False
    p_flg[1] = False
    p_tab = []
    if n == 2:
        p_tab.append(2)
    else:
        p = 3
        while p * p <= n:
            if p_flg[p]:
                for i in range(p, n//p+1, 2):
                    p_flg[p*i] = False
            p += 1
        p_tab = [2]
        for i in range(3, n+1, 2):
            if p_flg[i]:
                p_tab.append(i)
    res = [f[i] for i in range(n)]
    for i in p_tab:
        for j in range(n//i, 0, -1):
            res[i*j-1] -= res[j-1]
    return res
