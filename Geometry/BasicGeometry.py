def dist(p1, p2, squared=False):
    if len(p1) != len(p2):
        raise RuntimeError("invalid inputs: len({}) != len({})".format(p1, p2))
    res = 0
    n = len(p1)
    for i in range(n):
        res += (p1[i] - p2[i]) * (p1[i] - p2[i])
    if squared: return res
    return res**0.5

def intersection_point_same_radius(p1, p2, r):
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

def intersection_point(p1, p2, r1, r2):
    if p1 == p2:
        if r1 == r2:
            return (p1[0] + r1, p1[1])
        return None, None
    if dist(p1, p2, squared=True) > (r1 + r2) * (r1 + r2):
        return None, None
    if dist(p1, p2, squared=True) < (r1 - r2) * (r1 - r2):
        return None, None
    dd = dist(p1, p2, squared=True)
    kk = (4*r1*r1*dd - (r1*r1-r2*r2+dd)*(r1*r1-r2*r2+dd))/(4*dd*dd)
    if kk < 0:
        return None, None
    k = pow(kk, 0.5)
    mm = (r1*r1 - r2*r2 + dd) / (2*dd)
    px = (r1*r1-r2*r2)/(2*dd) * (p2[0] - p1[0]) + (p2[0] + p1[0]) / 2
    py = (r1*r1-r2*r2)/(2*dd) * (p2[1] - p1[1]) + (p2[1] + p1[1]) / 2
    p = (px, py)
    return (px - k * (p2[1] - p1[1]), py + k * (p2[0] - p1[0])), (px + k * (p2[1] - p1[1]), py - k * (p2[0] - p1[0]))
