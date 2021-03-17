def dist(p1, p2, squared=False):
    if len(p1) != len(p2):
        raise RuntimeError("invalid inputs: len({}) != len({})".format(p1, p2))
    res = 0
    n = len(p1)
    for i in range(n):
        res += (p1[i] - p2[i]) * (p1[i] - p2[i])
    if squared: return res
    return res**0.5

def intersection_point(p1, p2, r):
    if p1 == p2: return (p1[0] + r, p1[1])
    t = dist(p1, p2, squared=True)
    st = dist(p1, p2)
    h = ((2*r)*(2*r) - t)**0.5
    g = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
    X1 = (p2[1] - p1[1])*h*st/(2*t) + g[0]
    X2 = (p1[1] - p2[1])*h*st/(2*t) + g[0]
    Y1 = (p1[0] - p2[0])*h*st/(2*t) + g[1]
    Y2 = (p2[0] - p1[0])*h*st/(2*t) + g[1]
    return (X1, Y1), (X2, Y2)
