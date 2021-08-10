def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]
def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]
def getZone(base, v):
    ip = dot(base, v)
    op = cross(base, v)
    if ip > 0 and op == 0:
        return 8
    if ip > 0 and op > 0:
        return 1
    if ip == 0 and op > 0:
        return 2
    if ip < 0 and op > 0:
        return 3
    if ip < 0 and op == 0:
        return 4
    if ip < 0 and op < 0:
        return 5
    if ip == 0 and op < 0:
        return 6
    if ip > 0 and op < 0:
        return 7
    if ip == 0 and op == 0:
        return 8
def compareArgument(base, u, v):
    zu, zv = getZone(base, u), getZone(base, v)
    if zu < zv:
        return True
    elif zu > zv:
        return False
    op = cross(u, v)
    if op > 0:
        return True
    elif op < 0:
        return False
    if dot(u, u) <= dot(v, v):
        return True
    else:
        return False
def getConvexHull(points):
    n = len(points)
    imax = 0
    dmax = -1
    vec = (0, 0)
    for i in range(n):
        if dmax < points[i][0] * points[i][0] + points[i][1] * points[i][1]:
            dmax = points[i][0] * points[i][0] + points[i][1] * points[i][1]
            imax = i
            vec = (points[i][0], points[i][1])
    isUnvisited = [True]*n
    res = []
    center = imax
    prev = -1
    while isUnvisited[center]:
        isUnvisited[center] = False
        res.append(center)
        t = center
        mvec = (0, 0)
        d = dmax
        for i in range(n):
            if i == center or i == prev:
                continue
            v = (points[i][0] - points[center][0], points[i][1] - points[center][1])
            if v[0] == 0 and v[1] == 0:
                continue
            if compareArgument(vec, v, mvec):
                mvec = v
                t = i
        vec = (points[center][0] - points[t][0], points[center][1] - points[t][1])
        prev = center
        center = t
    return res
