def floor_sum(n, m, a, b):
    res = n*(n-1)*(a//m)//2+n*(b//m)
    a %= m
    b %= m
    s, t, u, v = n, m, a, b
    while u:
        s, t, u, v = (u*s+v)//t, u, t, (u*s+v)%t
        res += s*(s-1)*(u//t)//2+s*(v//t)
        u %= t
        v %= t
    return res
